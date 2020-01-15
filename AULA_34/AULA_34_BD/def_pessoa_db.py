import MySQLdb

def listar_todos():
    
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd= '')  # -- AQUI CONFIGURA A CONEXÃO 
    cursor = conexao.cursor() # -- AQUI SALVA O CURSOR DA CONEXÃO EM UMA VARIÁVEL 

    comando_sql = "SELECT * FROM aulabd.dados_pessoa" # --  CRIAÇÃO DE COMANDO SQL E PASSANDO PARA O CURSOR
    cursor.execute(comando_sql)

    resultado = cursor.fetchall()  # -- AQUI RETORNA UMA TUPLA -- SE TIVER MAIS DADOS SERA RETORNADO UMA LISTA DE TUPLAS

    return resultado