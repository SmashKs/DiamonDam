from flask import Flask
from flask_restplus import Api

from rest_api.v1.controllers.test import test


def layout_mongo(app: Flask):
    app.config.update(MONGO_URI='mongodb://localhost:7192/local')


def draw_routing(app: Flask):
    app.register_blueprint(test, url_prefix='/test')


def swagger_conf(api: Api, app: Flask):
    api.init_app(app)
