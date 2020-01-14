import MySQLdb



def ler_dados():
    arq = open('C:\\Users\\900139\\Desktop\\GIT\\PYTHON_COURSE\\AULA_33\\dados_pessoas_2.txt','r', encoding="utf-8")
    lista = []
    for pessoa in arq:
       a = pessoa.strip()
       b = a.split(';')
       lista.append(b)
    arq.close()
    return lista


def salvar_dados(cursor, connection,lista_de_dados):
    
    for p in lista_de_dados:
        cursor.execute(f"INSERT INTO dados_pessoa (ID, NOME, IDADE, SEXO, EMAIL, TELEFONE) VALUES ({p[0]}, '{p[1]}', {p[2]}, '{p[3]}', '{p[4]}', '{p[5]}')")
        connection.commit()


connection = MySQLdb.connect(host='localhost', database='db_teste', user='root', passwd='')

cursor = connection.cursor()

lista_dados = ler_dados()

print(lista_dados)

#salvar_dados(cursor, connection, lista_dados)