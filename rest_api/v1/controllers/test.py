from flask import Blueprint

test = Blueprint('test.api', __name__)


@test.route('/ttt')
def test123():
    # print('debug ->', c_mongo)
    # collection = client.db
    # print('debug ->', collection)
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
    # collection.insert(student)
    return student
