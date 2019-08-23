from flask_restplus import Resource

from rest_api.apis import api


@api.route('/<string:id>')
class HelloWorld(Resource):
    def get(self, id):
        return {id: 'world'}
