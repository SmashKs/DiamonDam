from flask import Config, Flask

from rest_api.v1.apis import api


def create_app(conf: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(conf)
    app.config.update(
            MONGO_HOST='localhost',
            MONGO_PORT=7192,
            # MONGO_USERNAME='bjhee',
            # MONGO_PASSWORD='111111',
            # MONGO_DBNAME='flask'
    )
    api.init_app(app)

    return app
