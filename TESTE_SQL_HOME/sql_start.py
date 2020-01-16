import MySQLdb

def insert_values (cursor, connection):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    profissao = input('Digite a profissão: ')
    comando_sql = f"INSERT INTO aula_database.pessoa_dados (NOME, IDADE, PROFISSAO) VALUES ('{nome}',{idade},'{profissao}');"

    cursor.execute(comando_sql)
    connection.commit()

def listar (cursor, connection):
    cursor.execute('SELECT * FROM aula_database.pessoa_dados')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(f'{p}')    

def atualizar (cursor, connection):
    id = int(input('Digite o ID que deseja atualizar: '))
    nome = input('Digite o novo nome: ')
    idade = int(input('Digite a nova idade: '))
    profissao = input('Digite a nova profissão: ')
    comando_update = f"UPDATE aula_database.pessoa_dados SET NOME='{nome}', IDADE={idade}, PROFISSAO ='{profissao}' WHERE ID={id}; "
    
    cursor.execute(comando_update)
    connection.commit()

    
connection = MySQLdb.connect(host='localhost', database='aula_database', user='root', passwd='root123')

cursor = connection.cursor()

# insert_values(cursor,connection)
atualizar(cursor,connection)
