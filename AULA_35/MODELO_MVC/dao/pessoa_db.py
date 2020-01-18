import MySQLdb

from model.pessoa import Pessoa

class PessoaDb:
    #-- Configurar a conexão
    connection = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    # -- Salvar um cursor para a conexão
    cursor = connection.cursor()
    
    def listar_todos(self):
        # --  Comando Sql que vai ser passado para o cursor
        comando_sql_select = 'SELECT * FROM aulabd.dados_pessoa'
        # -- Execução do comando Sql
        self.cursor.execute(comando_sql_select)
        # -- Aqui pega o resultado da execução do comando e salva na variavel resultado
        resultado = self.cursor.fetchall() # -- resultado retorna como uma lista de tuplas
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe #-- Aqui retorna o resultado
    
    def buscar_por_id(self, id):
        #-- Criando o comando sql para passar para cursor
        comando_sql_select = f'SELECT * FROM aulabd.dados_pessoa WHERE id ={id}'
        # -- Execução do comando Sql
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone() # -- Salva o resultado da execução na variavel -- Retorna apenas um dados que é uma tupla
        return resultado # -- Aqui retorna o Resultado
    
    def converter_tabela_classe(self, lista_tuplas):
        # -- Aqui cria uma lista para armazenar os dicionarios
        lista_pessoas = []
        for p in lista_tuplas:
            p1 = Pessoa() #--- Aqui cria o objeto(p1) da classe Pessoa()
            p1.id = p[0]   #-- Identifica cada posição da tupla pelo indice e é atribuido como chave no dicionario
            p1.nome = p[1]
            p1.sobrenome = p[2]
            p1.idade = p[3]
            p1.endereco_id = [4]
            lista_pessoas.append(p1)
            
        return lista_pessoas #-- Aqui retorna a lista que contém o dicionario com os dados
    