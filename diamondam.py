from rest_api import create_app
from rest_api.config import DevConfig

app = create_app(DevConfig)

print('debug ->', app.url_map)

# @app.route('/<string:id>')
# class HelloWorld(Resource):
#     def get(self, id):
#         return {id: '321'}
