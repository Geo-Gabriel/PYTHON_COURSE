import MySQLdb
from Model.endereco import Endereco

class EnderecoDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='root123')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM aulabd.endereço"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM aulabd.endereço WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, endereco:Endereco):
        comando = f""" INSERT INTO aulabd.endereço
        (
            RUA,
            BAIRRO,
            NUMERO,
            CEP,
            CIDADE,
            ESTADO
        )
        VALUES
        (
            '{endereco.rua}',
            '{endereco.bairro}',
            '{endereco.numero}',
            '{endereco.cep}',
            '{endereco.cidade}',
            '{endereco.estado}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, endereco:Endereco):
        comando = f""" UPDATE aulabd.endereço
        SET
            RUA = '{endereco.rua}',
            BAIRRO = '{endereco.bairro}',
            NUMERO = '{endereco.numero}',
            CEP = '{endereco.cep}',
            CIDADE = '{endereco.cidade}',
            ESTADO = '{endereco.estado}'
        WHERE ID = {endereco.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE aulabd.endereço WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
        