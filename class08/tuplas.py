# Aula 08 - 18-11-2019
# TUPLAS

numeros = [1,4,6]
usuario = {'nome':'user','password':123456}
pessoa = ('george','gabriel', 0, 0.45, numeros)


numeros[1] = 5
usuario ['password'] = 456123
# print(pessoa[2])

# print(numeros)
# print(usuario)
# print(pessoa)

lista_pessoas = []
lista_pessoas.append(pessoa) # posso ter varias tuplas dentro de uma lista

numeros[1]  = 5
pessoa[4][1] = 6
# print(pessoa[4][1])

# nome_completo = ' george' ' ' 'gabriel'

# print((nome_completo).count('g'))
# print((nome_completo).upper()) 
# print((nome_completo).lower()) 
# print((nome_completo).strip().split('a'))

# print((nome_completo).capitalize())

pessoa = [" ", "Lindo","bonito"]
# print(pessoa)
# print((' nem ').join(pessoa))
# frase = 'Geo Gab'
# print((' a ').join(frase))
frase = 'George' ' Gabriel'
print(pessoa[:2])
print(pessoa)
print(pessoa.count('Bonito'))