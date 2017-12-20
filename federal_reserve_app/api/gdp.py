from flask import Blueprint, jsonify
from flask_restplus import Api, Resource
from extensions import fred
import pandas as pd

blueprint = Blueprint('gdp', __name__, url_prefix='/api')
api = Api(blueprint)



@api.route("/load/<series_id>",  methods=['GET'])
@api.param('series_id', 'The series identifier')
class load(Resource):
    def get(self,series_id):
        data = fred.get_series(series_id)
        fred.load(data, 1, 'replace')
        return jsonify({'load': 'success'})

@api.route("/increment/<seriesid>",  methods=['GET'])
@api.param('series id', 'The series identifier')
class increment(Resource):
    def get(self):
        return jsonify({'load': 'success'})