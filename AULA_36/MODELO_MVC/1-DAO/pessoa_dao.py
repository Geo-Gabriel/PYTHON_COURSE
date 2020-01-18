import MySQLdb

from model.pessoa import Pessoa

class PessoaDao:
    connection = MySQLdb.connect(host='local', database='aulabd', user='root', passwd='')
    cursor = connection.cursor() 
    
    def listar_todos(self):
        comando = f"SELECT * FROM aulabd.endereco"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self, id):
        comando = f"SELECT * FROM aulabd.endereco WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, pessoa: Pessoa)
        comando = f'''INSERT INTO aulabd.pessoa 
        (
            NOME,
            SOBRENOME,
            IDADE,
            ENDERECO_ID
        )
        
        VALUES
        (
            '{pessoa.id}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereco_id}
        )
        '''
        
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def alterar(self, pessoa:Pessoa):
        comando = f'''UPDATE aulabd.pessoa 
        SET
            NOME = '{pessoa.nome}',
            SOBRENOME = '{pessoa.sobrenome}',
            IDADE  = {pessoa.idade},
            ENDERECO_ID = {pessoa.endereco_id},
            
        
        '''
              
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def deletar (self, pessoa:Pessoa):
        pass
    