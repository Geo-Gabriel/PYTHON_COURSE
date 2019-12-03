# Faça um programa que leia um numero inteiro de 1 a 100 no teclado e 
# mostre se você acertou ou
# o numero digitado é maior ou menor.
# Quando você acertar o programa deve ser finalizado

from random import randint
aleatorio = randint(1,10)
print(aleatorio)

numero = 0

while not numero == aleatorio:
    numero = int(input('Digite um número: '))
    if numero > aleatorio:
        print('O número é maior!')
    elif numero < aleatorio:
        print('O número é menor!')
    else:
        print('Você acertou!')


