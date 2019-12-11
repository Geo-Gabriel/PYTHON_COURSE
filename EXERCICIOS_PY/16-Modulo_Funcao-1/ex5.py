#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

radical = ''
indice = ''

def calc_raiz (a,b):
    a = int(input('Digite a (radicando): '))
    b = int(input('Digite b (indice): '))
    raiz = (a ** (1/b))
    return raiz

print(f'A raiz é {calc_raiz(radical,indice)}')