from flask import jsonify, request
from x.edbhs.users import blueprint
from flask_restful import Api, Resource

api = Api(blueprint)


@blueprint.route('/', methods=['GET'])
def index():
    response = {
        'msg': 'Hello World'
    }
    return jsonify(response);


class Users(Resource):

    def get(self, id=None):
        return 'Hi there another'

    def post(self):
        pass


api.add_resource(Users, '/another')
