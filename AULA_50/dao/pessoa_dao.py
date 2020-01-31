import MySQLdb

class PessoaDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', )
        self.cursor = self.connection.cursor()

    def list_all(self):
        return 'Listando Pessoas'

    def get_by_id(self, id):
        return f'Retornando pessoa pelo ID: {id}'

    def insert_pessoa(self, pessoa):
        return f'Inserindo pessoa: {pessoa}'

    def update_pessoa(self, pessoa):
        return f'Alterando pessoa: {pessoa}'

    def remove(self, id):
        return f'Removendo pessoa pelo id: {id}'
