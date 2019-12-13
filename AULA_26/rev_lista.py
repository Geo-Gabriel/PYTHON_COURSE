# Aula 21 - 13-12-2019

Funções para lista.

Estas funções ajudam no trabalho com as listas:

min(), max(), sum(), len()

min() ele retorna o menor valor de uma lista.
Esta função funciona para números quanto para alfabeto.


lista_numerica = [2,4,1,5,6,7,3]
lista_alfabetica = ['a','b','d','g']

print( min(lista_numerica) ) #o numero 1
print( min(lista_alfabetica) )#o caracter 'a'

max() ele retorna o maior valor dentro de uma lisa.
Esta função funciona para números quanto para alfabeto.

print( max(lista_numerica) ) #o numero 7
print( max(lista_alfabetica) )#o caracter 'g'

sum() faz a soma de todos os valores dentro da lista. Estes valore devem ser
númericos para que esta função funcione.

print( sum(lista_numerica) ) #o numero 28

len() ele conta quantos itens tem um objeto como caracteres de uma string,
bytes, tupla, lista, dicionário. 

print( len(lista_alfabetica) ) #o resultado é 4 item
print( len(lista_numerica) ) #o resultado é 7 itens



Há dois operadores relacionas que podem ser usados em qualquer objetos do
pythom. No cao da lista eles podem ajudar e muito.

Operador in
Este operado verifica se o iten faz parte da lista.
Exemplo:
lista = [0,1,2,3,4,5,6,7,8,9]

>>> 5 in lista
True
>>> 10 in lista_alfabeticaFalse

Este metodo também pode verificar se há algum caracter em uma string

>>> 'a' in 'Agua mole pedra dura'
True
>>> 'b' i 'Agua mole pedra dura'
False

Operador is

Este operador verifica se o item é o mesmo. Em outras palavras, verifica
se as variáveis estão apontando para o mesmo local da memória.
Para entender este conceito devemos notar que:

o comando id() retorna o local da memória em que está guardada a variável.

Criando e verificando o endereço da lista
>>> lista = [1,2,3]
>>> id(lista)
140534041888960


Criando a lista_numero e atribuindo a lista
Neste ponto as duas variáveis passam a apontar a mesma lista na memória.
Isso pode ser notado olhando o id() das duas.

>>> lista_numero = lista
>>> id(lista)
140534041888960
>>> id (lista_numero)
140534041888960

Como as duas variáveis são uma lista só então é de se esperar que elas sejam
iguais.

>>> lista == lista_numero
True

Aqui verificamos se a lista é a lista_numero. o is irá retornar True se as 
duas listas estão apontando para a mesma localidade na memória.

>>> lista is lista_numero
True

Aqui entra a diferença entre is e ==.
Fazendo uma cópia da lista e atribuindo para a lista_numero estamos "criando"
uma lista nova com os mesmos dados.
Isso é notado olhand o id() das duas listas.

>>> lista_numero = lista.copy()
>>> id (lista_numero)
140534041873776
>>> id(lista)
140534041888960


Para testar, vemos os valores das duas listas. Nota-se que são iguais. Porem
a localidade da memória é diferente. Assim a operação == (igual) mostra 
que as duas listas são iguais e o operador is mostra que as mesmas são listas 
distintas.

>>> lista_numero
[1, 2, 3]
>>> lista
[1, 2, 3]
>>> lista == lista_numero
True
>>> lista is lista_numero
False

Qual a importância disso?

Ao alterar uma lista que aponta para o mesmo local que outra lista, as duas listas
seão alteradas.
Porem ao copiar a lista, as duas passam a ser listas diferentes e a alteração 
de uma lista não afeta a outra lista.