from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

class PessoaController:
    people = Pessoa()
    p_db = PessoaDb()
    
    def listar_todos(self):
        return self.p_db.listar_todos
    
    def exportar (self):
        listar_pessoa_controller = self.p_db.listar_todos()
        return self.people.exportar_arq(listar_pessoa_controller)
    