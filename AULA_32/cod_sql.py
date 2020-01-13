# REFERENCIAS AO MYSQL


import MySQLdb

# -------------------------- FAZ A CONEXÃO COM O BANCO DE DADOS, PASSANDO OS DADOS DE LOGIN ------------------

def listar_todos(c):
    c.execute('SELECT * FROM dados_pessoa')
    pessoas = c.fetchall()
    for p in pessoas:
        print(f'\n{p}\n')


def buscar_id (c, id):
    c.execute(f'SELECT * FROM dados_pessoa WHERE ID_PESSOA={id}')
    pessoa = c.fetchone()
    print(pessoa)
    
def add_values (connection,c, endereco, nome, sobrenome, idade):
    cursor.execute (f"INSERT INTO aulabd.dados_pessoa (ENDEREÇO, NOME, SOBRENOME, IDADE) VALUES ({endereco},'{nome}', '{sobrenome}', {idade});")
    connection.commit() ## Manda os dados para o DB

connection = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')



cursor = connection.cursor()

add_values(connection, cursor, 3, 'Izabell', 'Plotka', 21)

listar_todos(cursor)

# buscar_id(cursor, (int(input('Digite id: '))))