#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

company = 'SMOOK WORLD'


def cabecalho (a):
    print ('=-=' * 20)
    print(f'                      {a}')
    print ('=-=' * 20)
    print(''' Seja bem vindo(a) a SMOOK WORLD sua loja de cingarros para ti dar carse 
    Beneficios de fumar: 
    1 - Dentes amarelos
    2 - Mau hálito
    3 - Cheiro de cingarro
    4 - Morre mais rápido
    5 - Menos um pra poluir o meio ambiente com essa chaminé ''')
    return(a)
cabecalho(company)