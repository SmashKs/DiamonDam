from flask import Flask
from flask_restplus import Resource

from rest_api.apis import api
from rest_api.config import DevConfig

app = Flask(__name__)


@api.route('/<string:id>')
class HelloWorld(Resource):
    def get(self, id):
        return {id: 'world'}


def initialize_app(flask_app: Flask):
    api.init_app(flask_app)


def main():
    app.config.from_object(DevConfig)
    initialize_app(app)
    app.run()


if __name__ == '__main__':
    main()
