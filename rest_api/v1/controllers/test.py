from flask_redis import FlaskRedis

import rest_api  # import from __init__, always needs to import package name then use.
from rest_api.v1.controllers import test


@test.route('/ttt')
def test123():
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
    print('debug ->', rest_api.mongo.db.reputation.find({}))
    redis = rest_api.rc  # type: FlaskRedis
    print('debug ->', redis.exists('student'), redis.exists('students'))
    print('debug ->', redis.get('student').decode('utf-8'))
    print('warn ->', redis.set('student', str(student)))
    return student
