from flask import Blueprint, jsonify
from flask_restplus import Api, Resource

blueprint = Blueprint('gdp', __name__, url_prefix='/api')
api = Api(blueprint)


@api.route("/gdp/load",  methods=['GET'])
class load(Resource):
    def get(self):
        return jsonify({'laod': 'success'})

@api.route("/gdp/increment",  methods=['GET'])
class increment(Resource):
    def get(self):
        return {'increment successful'}