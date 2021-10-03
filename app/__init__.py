import os
import googlemaps
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from .config import configs

env = os.environ.get("FLASK_ENV", "development")
mongo = PyMongo()
rest_api = Api()
gmaps = googlemaps.Client(key=configs[env].GOOGLE_MAP_API_KEY)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs[env])
    register_extensions(app)
    return app


def register_extensions(app):
    mongo.init_app(app)
    rest_api.init_app(app)

import app.routes  # set url routes