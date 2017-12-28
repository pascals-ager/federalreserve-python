from flask import Blueprint, jsonify, make_response, current_app
from flask_restplus import Api, Resource
from extensions.extract import ExtractAndLoad
from sqlalchemy import create_engine
import psycopg2

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
    _pos = 1
    _load_type = 'replace'
    
    
    def get(self,series_id):
        database_uri = current_app.config['DATABASE_URI']
        api_key = current_app.config['API_KEY']
        engine = create_engine(database_uri)
        schema = current_app.config['SCHEMA']
        try:
            table = Table(series_id).name
        except:
            return make_response('Unsupported series', 401, {'WWW-Authenticate' : 'Series not supported. Please select one of GDPC1, UMCSENT, or UNRATE'})
        etl = ExtractAndLoad(api_key, engine)
        data = etl.get_series(series_id)
        etl.load(data, self._pos, self._load_type, table, schema)
        return jsonify({'load': 'success'})

@api.route("/increment/<series_id>",  methods=['GET'])
@api.param('series_id', 'The series identifier')
class increment(Resource):
    _pos = 1
    _load_type = 'append'
    

    def get(self,series_id):
        database_uri = current_app.config['DATABASE_URI']
        api_key = current_app.config['API_KEY']
        engine = create_engine(database_uri)
        schema = current_app.config['SCHEMA']
        try:
            table = Table(series_id).name
        except:
            return make_response('Unsupported series', 401, {'WWW-Authenticate' : 'Series not supported. Please select one of GDPC1, UMCSENT, or UNRATE'})
        etl = ExtractAndLoad(api_key, engine)
        self._pos, start_date = etl.get_connection_point(table, schema)
        data = etl.get_series(series_id, start_date)
        etl.load(data, self._pos, self._load_type, table, schema)
        return jsonify({'load': 'success'})

