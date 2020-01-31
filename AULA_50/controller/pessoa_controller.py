from flask_restful import Resource

class PessoaController(Resource):

    def get (self):
        return 'Acessando metodo HTTP GET'

    def post (self):
        return 'Acessando metodo HTTP POST'

    def put (self):
        return 'Acessando metodo HTTP PUT'

    @property
    def delte (self):
        return 'Acessando metodo HTTP DELETE'
