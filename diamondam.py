from flask_pymongo import PyMongo

from rest_api import create_app
from rest_api.config import DevConfig

app = create_app(DevConfig)

print('debug ->', app.url_map)
c_mongo = PyMongo(app)

# r = redis.Redis(host='localhost', port=8174)

# @app.route('/<string:id>')
# class HelloWorld(Resource):
#     def get(self, id):
#         return {id: '321'}
