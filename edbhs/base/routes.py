from flask import jsonify, request
from x.edbhs.base import blueprint
from flask_restful import Api, Resource

api = Api(blueprint)


@blueprint.route('/', methods=['GET'])
def index():
    response = {
        'msg': 'Hello World base'
    }
    return jsonify(response);


class Base(Resource):

    def get(self, id=None):
        return 'Hi there another'

    def post(self):
        pass


api.add_resource(Base, '/another')
