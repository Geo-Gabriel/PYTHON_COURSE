# REFERENCIAS AO MYSQL

import MySQLdb

# --- MÉTODO QUE LISTA OS DADOS NA TABELA

def listar_todos(cursor):
    cursor.execute('SELECT * FROM dados_pessoa')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(f'\n{p}\n')


# --- MÉTODO QUE BUSCA PESSOAS POR ID

def buscar_id (cursor, id):
    cursor.execute(f'SELECT * FROM dados_pessoa WHERE ID_PESSOA={id}')
    pessoa = cursor.fetchone()
    print(pessoa)
    
    
# --- MÉTODO QUE BUSCA PESSOAS PELO SOBRENOME

def buscar_por_sobrenome(cursor, sobrenome):
    cursor.execute(f"SELECT * FROM aulabd.dados_pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  cursor.fetchall():
        print(p)    
    
    
# --- MÉTODO QUE SALVA DADOS EM UMA TABELA

def salvar(connection ,cursor, nome, sobrenome, idade, endereco=None):
    if endereco == None:
        endereco = 'NULL'
    cursor.execute (f"INSERT INTO aulabd.dados_pessoa (ENDEREÇO, NOME, SOBRENOME, IDADE) VALUES ({endereco},'{nome}', '{sobrenome}', {idade});")
    connection.commit() # --- O MÉTODO COMMIT() SALVA OS DADOS NA DATABASE


# --- MÉTODO QUE ALTERA DADOS EM UMA TABELA

def alterar (id,connection,cursor, nome, sobrenome, idade, endereco_id='NULL'):
    cursor.execute(f"UPDATE aulabd.dados_pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDEREÇO={endereco_id} WHERE ID_PESSOA={id} ")
    connection.commit()



# --- MÉTODO QUE DELETA DADOS EM UMA TABELA

def deletar_dados (connection,cursor,id):
    cursor.execute(f"DELETE FROM aulabd.dados_pessoa WHERE ID_PESSOA = {id}")
    connection.commit()



# ----------------------------- FAZ A CONEXÃO COM O BANCO DE DADOS, PASSANDO OS DADOS DE LOGIN --------------------------

connection = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='') # -- REALIZA A CONEXÃO COM O BANCO DE DADOS

cursor = connection.cursor() # -- CURSOS PARA NAVEGAR ENTRE OS DADOS


                                        # CHAMADA (TESTANDO) DOS MÉTODOS #



#--------------------- SALVAR REGISTRO -------------------------------------

# nome = input('Digite o nome: ')
# sobrenome = input('Digite o sobrenome: ')
# idade = int(input('Digite a idade: '))
# id_endereco = int(input('Digite o id do address: '))

#salvar(connection, cursor, nome, sobrenome, idade, id_endereco)

#--------------------- PESQUISA ID --------------------------------

# pesquisa_id = int(input('Digite o ID que deseja pesquisar: '))

# buscar_id(cursor, pesquisa_id)

#--------------------- PESQUISA SOBRENOME -----------------------------

# pesquisa_sobrenome = input('Digite o sobrenome para pesquisar: ')

# buscar_por_sobrenome(cursor, pesquisa_sobrenome)

#------------------------- ATUALIZAR --------------------------------------

# id_upd = int(input('Digite o ID do registro que deseja alterar: '))
# nome_upd = input('Digite o novo nome: ')
# sobrenome_upd = input('Digite o novo sobrenome: ')
# idade_upd = int(input('Digite a nova idade: '))
# endereco_upd = input('Digite o novo id_endereço: ')

# alterar (id_upd, connection, cursor, nome_upd, sobrenome_upd, idade_upd, endereco_upd)

#------------------------- DELETAR -------------------------------------

# id_delete = int(input('Digite o ID para deletar o registro: '))

# deletar_dados(connection, cursor, id_delete)

#----------------------- LISTAR TODOS OS DADOS ------------------------------------

# listar_todos(cursor)