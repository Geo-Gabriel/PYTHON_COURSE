#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

n = int(input('Digite um número para ver sua tabuada do 0 ao 10: '))

for i in range (0,11):
    print(f' {n} x {i} = {i*n}')