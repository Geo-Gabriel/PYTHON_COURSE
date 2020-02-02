import MySQLdb

from AULA_50.model.pessoa_model import PessoaModel


class PessoaDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='root', database='teste_api', passwd='root123')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute('SELECT * FROM teste_api.pessoas')
        resultado = self.cursor.fetchall()
        return resultado

    def get_by_id(self, id):
        self.cursor.execute(f'SELECT * FROM teste_api.pessoas WHERE id= {id}')
        pessoa = self.cursor.fetchone()
        return pessoa

    def insert_pessoa(self,nome, sobrenome, idade):
        self.cursor.execute(f"INSERT INTO teste_api.pessoas (nome, sobrenome, idade) VALUES ('{nome}', '{sobrenome}',{idade})")
        self.connection.commit()

    def update_pessoa(self, pessoa=PessoaModel):
        self.cursor.execute(f'''UPDATE teste_api.pessoas 
        id = {pessoa.id},
        nome = '{pessoa.nome}'
        sobrenome = '{pessoa.sobrenome}'
        idade = {pessoa.idade}
        ''')
        self.connection.commit()

    def remove(self, id):
        self.cursor.execute(f'DELETE FROM teste_api WHERE id= {id}')
        self.connection.commit()
        return f'Removido pessoa de id: {id}'


# p = PessoaModel
# dao = PessoaDao
#
# p.id = ''
# p.nome = input('Digite nome da pessoa: ')
# p.sobrenome = input('Digite sobrenome da pessoa: ')
# p.idade = int(input('Digite idade da pessoa: '))

dao = PessoaDao
# dao.insert_pessoa('Teste', 'Teste', 56, 56)

res = dao.list_all()
print(res)