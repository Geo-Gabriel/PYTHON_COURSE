from flask_restful import Resource
from AULA_50.dao.pessoa_dao import PessoaDao


class PessoaController(Resource):

    def __init__(self):
        self.dao = PessoaDao()

    def get (self):
        msg = self.dao.list_all()
        return msg

    def post (self):
        msg = self.dao.insert_pessoa('George')
        return msg

    def put (self):
        msg = self.dao.update_pessoa('Gabriel')
        return msg

    def delete (self):
        msg = self.dao.remove(10)
        return msg
