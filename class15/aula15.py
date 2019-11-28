# Aula 15 -- 28-11-2019
# manipulação de arquivos


def salvar_pessoa (pessoa_dicio):
    arq = open('nome.txt', 'a')
    arq.write(f"{pessoa_dicio['nome']};{pessoa_dicio['sobrenome']};{pessoa_dicio['idade']}\n")
    arq.close()

def ler ():
    lista = []
    arq = open('nome.txt', 'r')
    for linha in arq:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome': lista_linha[0], 'sobrenome': lista_linha[1], 'idade': lista_linha[2]}
        # print(lista_linha)
        lista.append(pessoa)
    arq.close()
    return lista


# nome = input('Digite nome: ')
# sobrenome = input('Digite sobrenome: ')
# idade = int(input('Digite sua idade: '))

# pessoa = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade} #f'{nome};{sobrenome};{idade}'

# salvar_pessoa(pessoa)


for pessoas in ler():
    print(f"{pessoas['nome']} - {pessoas['sobrenome']} - {pessoas ['idade']}")
