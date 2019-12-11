#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console


variavel = '===---'

def cabecalho (a):
    print (a * 20)
    print ('{}Bem vindo ao MUUNDO PARALELO & CIA DAS GALAXIA'.format('\t'*4))
    print (a * 20)
    print( '\n' * 20)
    return()


def rodape (a):
    print (a * 20)
    print ('{}Este é um rodapé que vai rodar seu pé e também seu novo amigo'.format('\t'*3))
    print (a * 20)
    return()

cabecalho(variavel)
rodape(variavel)