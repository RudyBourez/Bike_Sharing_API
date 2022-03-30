from flask import Flask
from flask_restful import Api
from API.resources.model import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')
