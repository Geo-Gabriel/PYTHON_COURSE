#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def sistema (a,b):
    print (f'{a * 20}\n \t\t\t\t\t {b}\n {a * 20}')

cabecalho = '===---'
nome_sistema = 'SMOOKS GALAXY Z'

sistema(cabecalho, nome_sistema)