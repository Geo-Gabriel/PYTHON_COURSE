# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como default ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

print(a)
print(b)
print(c)
print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.


lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).

print ('\t------------------------------ 1 -----------------------------------')

if lista[0] is lista[1]:
    print('As listas são as mesmas')
elif lista[0] == lista[1]:
    print('As listas são iguais')
else:
    print('As listas não são iguais nem as mesmas')


# 2) Qual é o maior valor destas duas listas 

print ('\t------------------------------ 2 -----------------------------------')

soma = (lista[0]) + (lista[1])
print(max(soma))

# 3) Qual é o maior valor de cada lista

print ('\t------------------------------ 3-----------------------------------')

print(f'Max lista1: {max(lista[0])} -- Max lista2: {max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?

print ('\t------------------------------ 4 -----------------------------------')

print(f'Há o número 10 na lista[0] >> {10 in lista[0]}')

# 5) Há o número 20 dentro da lista[1]?

print ('\t------------------------------ 5 -----------------------------------')

print(f'Há o número 20 na lista[1] >> {20 in lista[1]}')

# 6) Quantos números da lista[0] tem dentro da lista[1]?

print ('\t------------------------------ 6 -----------------------------------')

n = 0 
j = 0
s = 0

for n in lista[0]:
    if n == lista[1][j]:
        print(f'São iguais >> {n} contido em lista[0] e {lista[1][j]} contido em lista[1]')
        j = j + 1
print(f'elementos iguais: {len(lista[0])}')


# 7) Mostre os números da lista[0] que estão dentro da lista[1]

print ('\t------------------------------ 7 -----------------------------------')



# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

print ('\t------------------------------ 8 -----------------------------------')

soma = sum(lista[0])

for n in lista[1]:
    print(f'{soma * n}')

# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!

print ('\t------------------------------ 9 -----------------------------------')

soma = lista[0] + lista[1]
div = max(soma) // min(soma)
print(div)
if div in soma:
    print('Esta na lista')
else:
    print('Não esta na lista')

# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

print ('\t------------------------------ 10 -----------------------------------')

if max(lista[0]) in lista[1]:
    print(f'O maximo da lista0 esta na lista1: {max(lista[0])}')
else:
    print('O máximo da lista0 nao esta contido na lista1')
  
# =======================================================================================#

if min(lista[1]) in lista[0]:
    print(f'O min da lista1 esta na lista0: {min(lista[1])}')
else:
    print('O minimo da lista1 nao esta contido na lista0')