# Faça um programa que leia um numero inteiro de 1 a 100 no teclado e mostre
# se vc acertou ou não, o número digitado é maior ou menor, quando acertar o 
# o programa deve ser finalizado

from random import randint

n = randint(1,10)

print('''
===---===---===---===---===---===---===---===---===---===---===---===---===---
#                        JOGO DA ADVINHAÇÂO V1.0                             #
===---===---===---===---===---===---===---===---===---===---===---===---===---

                        (NÚMEROS DE 1 A 10)

''')

user = 0
tentativas = 1

while n != user:
    user = int(input('Digite sua advinha  >>  '))
    if user > n:
        print('Digite um número menor: \n  ')
        tentativas = tentativas + 1
    elif user < n:
        print('Digite um número maior: \n  ')
        tentativas = tentativas + 1
    else:
        print(f'\nParabéns você acertou !! -- O número era {n}')
        break

print(f'\nTotal de tentativas: {tentativas}')