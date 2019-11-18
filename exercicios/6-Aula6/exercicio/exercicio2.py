#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

#--- Resolução: Natan Caballero Dalmarco - 14-11-2019

numero = int(input('Digite um número inteiro: '))
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero}')