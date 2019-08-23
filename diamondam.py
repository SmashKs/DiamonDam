from rest_api import create_app
from rest_api.config import DevConfig

app = create_app(DevConfig)
