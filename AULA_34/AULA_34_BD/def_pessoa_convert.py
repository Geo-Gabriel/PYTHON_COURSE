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
