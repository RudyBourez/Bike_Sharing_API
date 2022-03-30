from flask_restful import Resource

class Model(Resource):
    def get(self, name):
        return {'Task': 'Say,'+ f'"Hello {name}!"'}