from flask import Blueprint, jsonify, make_response
from flask_restplus import Api, Resource
from extensions import etl


blueprint = Blueprint('Loading Fred Data', __name__, url_prefix='/api')
api = Api(blueprint)

from enum import Enum
class Table(Enum):
    gdp_data_stg = 'GDPC1'
    sentiment_idx_stg = 'UMCSENT'
    unemployment_rate_stg = 'UNRATE'


@api.route("/load/<series_id>",  methods=['GET'])
@api.param('series_id', 'The series identifier')
class load(Resource):
    def get(self,series_id):
        try:
            table = Table(series_id).name
        except:
            return make_response('Unsupported series', 401, {'WWW-Authenticate' : 'Series not supported. Please select one of GDPC1, UMCSENT, or UNRATE'})
        load_type = 'replace'
        pos = 1
        schema = 'fred'
        data = etl.get_series(series_id)
        etl.load(data, pos, load_type, table, schema )
        return jsonify({'load': 'success'})

@api.route("/increment/<series_id>",  methods=['GET'])
@api.param('series_id', 'The series identifier')
class increment(Resource):
    def get(self,series_id):
        try:
            table = Table(series_id).name
        except:
            return make_response('Unsupported series', 401, {'WWW-Authenticate' : 'Series not supported. Please select one of GDPC1, UMCSENT, or UNRATE'})
        load_type = 'append'
        pos = 1
        schema = 'fred'
        pos, start_date = etl.getConnectionPoint(table,schema)
        data = etl.get_series(series_id, start_date)
        etl.load(data, pos, load_type, table, schema )
        return jsonify({'load': 'success'})

