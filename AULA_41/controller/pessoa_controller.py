from flask_restful import Resource
import requests

class PessoaController(Resource):

    def get (self):
        cep = input('Digite cep: ')
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        endereco = r.json()
        return endereco

    def post (self):
        return 'Acessando metodo HTTP POST'

    def put (self):
        return 'Acessando metodo HTTP PUT'

    @property
    def delte (self):
        return 'Acessando metodo HTTP DELETE'
