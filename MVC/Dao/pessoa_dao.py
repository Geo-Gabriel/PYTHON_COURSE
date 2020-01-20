import MySQLdb
from Model.pessoa import Pessoa

class PessoaDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * aulabd.dados_pessoa AS P LEFT JOIN aulabd.endereço AS E ON P.endereço = E.ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM aulabd.dados_pessoa AS P LEFT JOIN aulabd.endereço AS E ON P.ENDEREÇO = E.ID_ENDEREÇO WHERE P.ID_PESSOA = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, pessoa:Pessoa):
        comando = f""" INSERT INTO aulabd.dados_pessoa
        (
            NOME,
            SOBRENOME,
            IDADE,
            ENDEREÇO
        )
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereço}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, pessoa:Pessoa):
        comando = f""" UPDATE aulabd.dados_pessoa
        SET
            NOME = '{pessoa.nome}',
            SOBRENOME ='{pessoa.sobrenome}',
            IDADE = {pessoa.idade},
            ENDEREÇO = {pessoa.endereco}
        WHERE ID = {pessoa.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM aulabd.dados_pessoa WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
        