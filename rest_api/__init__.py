from flask import Config, Flask

from rest_api.apis import api


def create_app(conf: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(conf)
    api.init_app(app)

    return app
