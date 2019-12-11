#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

# a = 0
# b = 0

# def numeros(a,b):
#     a = int(input('Digite a:'))
#     b = int(input('Digite b: '))
#     soma = a + b
#     return soma

# soma = numeros(a,b)
# print (f'O resultado da soma de a e b: {soma}')

# Resolução de acordo com o enunciado

def soma():
    a = int(input('Digite a: '))
    b = int(input('Digite b: '))
    adicao = a + b
    print(f'{a} + {b} = {adicao}')  #Aqui termina a resolução, para testar tem que chamar a função. 

soma()