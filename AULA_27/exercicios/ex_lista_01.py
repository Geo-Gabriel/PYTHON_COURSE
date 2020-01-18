# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint


lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,80))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?

print ('\t------------------------------ 1.1 -----------------------------------')

print(len(lista1))

# 1.2) Qual é o maior valor da lista2?
print ('\t------------------------------ 1.2 -----------------------------------')

print(max(lista2))


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?

print ('\t------------------------------ 1.3 -----------------------------------')

print(max(lista2) + min(lista2))


# 1.4) Qual é a média aritmética da lista1?

print ('\t------------------------------ 1.4 -----------------------------------')

print(sum(lista1) / len(lista1))


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)

print ('\t------------------------------ 1.5 -----------------------------------')

print(f'{sum(lista1)} - {sum(lista2)} - {sum(lista3)} - {(sum(lista1) + sum(lista2) + sum(lista3) )}')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.

print ('\t------------------------------ 1.6 -----------------------------------')

for i in lista1:
    print(f'{i}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError

print ('\t------------------------------ 1.7 -----------------------------------')

print()

try:
    print(f'LISTA1 --> pos5: {lista1[4]} -- pos9: {lista1[8]} -- pos10: {lista1[9]} -- pos25: {lista1[24]}')
    print(f'LISTA2 --> pos5: {lista2[4]} -- pos9: {lista2[8]} -- pos10: {lista2[9]} -- pos25: {lista2[24]}')
    print(f'LISTA3 --> pos5: {lista3[4]} -- pos9: {lista3[8]} -- pos10: {lista3[9]} -- pos25: {lista3[24]}')
except IndexError:
    print('<< Indexação errada!! >>')
finally:
    print('<< END >> ')

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).

print ('\t------------------------------ 1.8 -----------------------------------')


if len(lista1) > len(lista2) and len(lista3):
    print(f'LISTA1 contém mais itens: {len(lista1)}')
elif len(lista2) > len(lista1) and len(lista3):
    print(f"LISTA2 contém mais itens: {len(lista2)}")
elif len(lista3) > len(lista1) and len(lista2):
    print(f'LISTA3 contém mais itens: {len(lista3)}')
else:
    print('<< As tres listas contém a mesma quantidade de elementos >> ')

print()

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.

print ('\t------------------------------ 1.9 -----------------------------------')

soma = max(lista1) + max(lista2) + max(lista2)
l1 = min(lista1)
l2 = min(lista2)
l3 = min(lista3)

if l1 < l2 and l3:
    print(soma - l1)
elif l2 < l1 and l3:
    print(soma - l2)
elif l3 < l2 and l1:
    print(soma - l3)

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

print ('\t------------------------------ 1.10 -----------------------------------')

soma_lista = (lista1 + lista2 + lista3)


print(max(soma_lista) - min(soma_lista))

