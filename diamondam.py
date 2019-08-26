from flask_restplus import Resource

from rest_api import api, create_app
from rest_api.config import DevConfig

app = create_app(DevConfig)


@api.route('/<string:id>')
class HelloWorld(Resource):
    def get(self, id):
        return {id: 'world'}
