from flask import Config, Flask

from rest_api.settings import draw_routing, layout_mongo, swagger_conf
from rest_api.v1.apis import api
from rest_api.v1.controllers.test import test


def create_app(conf: Config) -> Flask:
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(conf)
    layout_mongo(app)
    draw_routing(app)
    swagger_conf(api, app)

    return app
