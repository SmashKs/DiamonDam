from flask import Flask
from flask_restplus import Api

from rest_api.v1.controllers import test


def layout_mongo(app: Flask):
    app.config.update(
            MONGO_URI='mongodb://localhost:7192/reputation',
            REDIS_URL='redis://localhost:8174/0'
    )
    # Here is later than init part.
    from rest_api import mongo
    mongo.init_app(app)


def build_redis(app: Flask):
    from rest_api import rc
    rc.init_app(app)


def draw_routing(app: Flask):
    app.register_blueprint(test, url_prefix='/test')


def swagger_conf(api: Api, app: Flask):
    api.init_app(app)
