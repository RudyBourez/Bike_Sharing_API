from pickle import APPEND
from flask import Flask
from flask_restful import Api
from API.resources.model import Model

app = Flask(__name__)
api = Api(app)

api.add_resource(Model, '/Model' ,'/Model/<string:name>')
