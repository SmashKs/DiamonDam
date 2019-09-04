from flask_restplus import Resource

from diamondam import mongo
from rest_api.v1.controllers import test


@test.route('/ttt/<string:id>')
class Fun(Resource):
    def get(self, id):
        print('debug ->', mongo)
        # collection = client.db
        # print('debug ->', collection)
        # student = {
        #     'id': '20170101',
        #     'name': 'Jordan',
        #     'age': 20,
        #     'gender': 'male'
        # }
        # collection.insert(student)
        return '1231421'
