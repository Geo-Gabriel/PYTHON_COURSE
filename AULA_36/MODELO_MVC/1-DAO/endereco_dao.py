import MySQLdb

from model.pessoa import Pessoa


class EnderecoDao:
  
    connection = MySQLdb.connect(host='local', database='aulabd', user='root', passwd='')
    cursor = connection.cursor()
    
    def listar_todos(self):
        comando = f"SELECT * FROM aulabd.endereco"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
    
    def buscar_id(self, id):
        comando = f"SELECT * FROM aulabd.endereco WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
    
    def salvar(self, endereco:Pessoa):
        comando = f'''INSERT INTO aulabd.pessoa 
        (
            NOME,
            SOBRENOME,
            IDADE,
            ENDERECO_ID
        )
        
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereco_id}
        )
        '''
        
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def alterar(self, endereco:Pessoa):
        pass
    
    def deletar (self, endereco:Pessoa):
        pass
    