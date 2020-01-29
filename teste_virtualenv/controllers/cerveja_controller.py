from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
        return 'Acessando metodo HTTP GET'
    def post(self):
        return 'Acessando metodo HTTP POST'
