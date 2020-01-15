# --- CLASSES 

import MySQLdb


def listar_todos():
    
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd= '')  # -- AQUI CONFIGURA A CONEXÃO 
    cursor = conexao.cursor() # -- AQUI SALVA O CURSOR DA CONEXÃO EM UMA VARIÁVEL 

    comando_sql = "SELECT * FROM aulabd.dados_pessoa" # --  CRIAÇÃO DE COMANDO SQL E PASSANDO PARA O CURSOR
    cursor.execute(comando_sql)

    resultado = cursor.fetchall()  # -- AQUI RETORNA UMA TUPLA -- SE TIVER MAIS DADOS SERA RETORNADO UMA LISTA DE TUPLAS

    return resultado


def converter_tabela_dic(lista_tuplas):
    
    lista_pessoas = []

    for p in lista_tuplas:
        dic_pessoa = {'ID': 0, 'NOME': '', 'SOBRENOME': '', 'IDADE': 0, 'ENDEREÇO': 0 }  # -- AQUI REPRESENTA OS DADOS DE UMA LINHA NA TEBELA
        dic_pessoa['ID'] = p[0]
        dic_pessoa['NOME'] = p[1]
        dic_pessoa['SOBRENOME'] = p[2]
        dic_pessoa['IDADE'] = p[3]
        dic_pessoa['ENDEREÇO'] = p[4]
        
        lista_pessoas.append(dic_pessoa)

    return lista_pessoas

# for p in lista_pessoas:
#     print(f"\t {p}")
    
def exportar_txt(lst_pessoas):
    
    with open('AULA_34/pessoas.txt', 'a') as arquivo:
        for p in lst_pessoas:
            arquivo.write(f"{p['ID']};{p['NOME']};{p['SOBRENOME']};{p['IDADE']};{p['ENDEREÇO']} \n")
            
lpt = listar_todos()

lpd = converter_tabela_dic(lpt)

exportar_txt(lpd)
    