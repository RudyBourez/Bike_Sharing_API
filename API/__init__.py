from flask import Flask
import pandas as pd
from flask_restful import Api
from API.resources.model import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello,'/', '/<string:json>')
