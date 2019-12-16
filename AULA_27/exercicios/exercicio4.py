# Aula 21 - 16-12-2019
# NÂO OBRIGATÓRIA - Para os alunos avançados!

# Com esta lista embaralhada... nem Zeus sabe o que tem nela!

from geradorlista import embaralhar_int_str_hard
from random import randint

lista = embaralhar_int_str_hard(randint(3,20),randint(10,50))

# Olhá só que encrenca:

# for i in lista:
#     print('\n',i)


# Crie um algoritmo que verifique se todas as listas dentro da "lista" são iguais ou são elas mesmas!
# No final, quantas listas são somente iguais e quantas listas são as mesmas.
# Mostre tambem os indices das listas que são eles mesnos (is) e os indices das listas que são somente 
# iguais

# Boa sorte!


# for i in lista:
#     print('\n',i)

print('\n')
iguais = 0
elamesma = 0
dic_is = {}
dic_ig = {}
for lento in range(len(lista)-1):
    lista_is = []
    lista_ig = []
    for rapido in range(lento+1,len(lista)):
        print(f'{lento} == {rapido} = {lista[lento] == lista[rapido]}')
        print(f'{lento} is {rapido} = {lista[lento] is lista[rapido]}')
        
        if lista[lento] is lista[rapido]:
            elamesma += 1
            lista_is.append(rapido)
        elif lista[lento] == lista[rapido]:
            iguais += 1
            lista_ig.append(rapido)
    dic_is[lento] = lista_is
    dic_ig[lento] = lista_ig
    print('\n')


print('Numero de listas is: ',elamesma)  
for i in dic_is:
    print(f'{i} : {dic_is[i]}')      
#print(dic_is,'\n')
print('Numero de listas iguais: ',iguais)
print(dic_ig,'\n')
for i in dic_ig:
    print(f'{i} : {dic_ig[i]}') 