# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.

# a = int(input('Digite a: '))
# b = int(input('Digite b: '))

# print(f'{a+b}, {a-b}, {a*b}, {a/b}')

# while True:
#     a = int(input('Digite a: '))
#     b = int(input('Digite b: '))
#     if a and b != int:
#         print('digite valido')
#     print(f'soma: {a+b}, sub: {a-b}, produto: {a*b}, div: {a/b}')

#     c = input('Deseja continuar? (qualquer tecla p/sim e "s" p/não): ')
#     if c == 's':
#         break

# controle = 'n'


while True:
    try:
        a = int(input('Digite a: '))
        b = int(input('Digite b: '))

    except ValueError:
        print('Digite um número inteiro  ;/')

    else:
        print(f'soma: {a+b}, sub: {a-b}, produto: {a*b}')

    try:
        print(f'div: {a/b}')

    except:

        print('div: Impossível dividir por zero')

    controle = input('Digite qualquer tecla p/ continuar ou "s" para sair: ')
    if controle == 's':
        print('GOOD--BYE')
        break



# while True:
#     try:
#         print('pass 1')
#         a = numero = int(input('Digite a: '))
#         print('pass 2')
#     except ValueError:
#         print('vc digitou errado fdp')
#     else:
#         print('FIMM!')
#         break