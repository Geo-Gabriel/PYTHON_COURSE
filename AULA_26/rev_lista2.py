# Aula 21 - 13-12-2019


Metodos para Lista:

Aqui vamos ver 90% dos metodos que podem ser usados
em listas. Estes metodos ajudam a trabalhar, alterar, filtrar qualquer elemento
de uma lista.

###################### .join() ######################

Já conhhecemos o elemento .split('') que pega uma string e quebra em uma lista. 
Agora vamos conhecer um comando que irá fazer o contrário. Este irá converter
uma lista em uma string.

É importante avisar que a lista deve ser composta por variáveis do tipo string. 
Caso haja um número (int, float) na lista ocorrerá o erro TypeError.
Funcionamento:

lista=['codigo','nome','idade','sexo']

Primerio deve determinar qual vai ser o caracter que irá separar os itens da lista. 
Neste caso vamos colocar o ';'

>>> ';'.join(lista)
'codigo;nome;idade;sexo'

Verificamos que retornou uma string conhecida ;-)

Neste caso, queremos que a lista seja separada por um espaço:

>>> ' '.join(lista)
'codigo nome idade sexo'

###################### .append() ######################


Para adicionar itens em uma lista, usamos o metodo .append() Como este foi
um metodo muito usado, vamos só dar uma passadinha rápida:


.append(objeto)
Adiciona objeto no final da lista

lista.append(1)
>>> lista
['codigo', 'nome', 'idade', 'sexo', 1]


###################### .copy() ######################

copy()
Faz uma cópia rasa da lista. Quando se fala de cópia rasa estamos dizendo que
ele cria uma cópia da primeira lista. Se por acaso houver listas dentro de listas,
as listas internas serão as mesmas. Se alterar-las as outras serão alteradas.

exemplo:

>>> lista_com_listas = [[1,2,3],['a','b','c']]
>>> lista_copia = lista_com_listas.copy()

>>> lista_com_listas == lista_copia
True
>>> lista_com_listas is lista_copia
False

>>> lista_com_listas[0].append('dado qualquer')

>>> lista_com_listas
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c']]
>>> lista_copia
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c']]

>>> lista_com_listas.append('Adicionando dado na lista rasa')

>>> lista_com_listas
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c'], 'Adicionando dado na lista rasa']
>>> lista_copia
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c']]


###################### copy.deepcopy() ######################

O deepcopy ele copia todas as listas quebrando qualquer vinculo com elas.
Assim chamamos de cópia profunda deepcopy!

Para usa-lo devemos importar a biblioteca copy

>>> import copy

Criando uma lista para teste:

>>> lista_com_listas = [[1,2,3],['a','b','c']]

Criando uma cópia profunda da lista.

>>> lista_copia = copy.deepcopy(lista_com_listas)

Verificando se as listas são as mesmas ou iguais

>>> lista_com_listas == lista_copia
True
>>> lista_com_listas is lista_copia
False

Adicionando um item dentro da lista e verificando se altera outra lista.

>>> lista_com_listas[0].append('dado qualquer')
>>> lista_com_listas
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c']]
>>> lista_copia
[[1, 2, 3], ['a', 'b', 'c']]

Até agora verificamos que a lista interna foi alterada mas a cópia não foi!

Vamos fazer mais um teste, criar mais listas dentro de outras listas.
Depois daremos um .append() na lista mais interna e verificar se o deepcopy
copia todas as listas.


>>> lista_com_listas
[[1, 2, 3, 'dado qualquer'], ['a', 'b', 'c']]
>>> lista_com_listas[0].append(['z','y',['g','h']])
>>> lista_com_listas
[[1, 2, 3, 'dado qualquer', ['z', 'y', ['g', 'h']]], ['a', 'b', 'c']]
>>> lista_copia = copy.deepcopy(lista_com_listas)
>>> lista_com_listas[0][4][2].append('listas profundas')
>>> lista_com_listas
[[1, 2, 3, 'dado qualquer', ['z', 'y', ['g', 'h', 'listas profundas']]], ['a', 'b', 'c']]
>>> lista_copia
[[1, 2, 3, 'dado qualquer', ['z', 'y', ['g', 'h']]], ['a', 'b', 'c']]
>>> 

###################### .count() ######################


count(valor)
Retorna o mumero de ocorrência de um determinado valor dentro da lista.

>>> lista = [1,2,3,'a','b','c',3,'a',3]
>>> lista.count(3)
3

Atenção: Ele só irá retornar a contagem se o valor estiver na lista rasa. 
Se o dado estiver dentro de outra lista o count() não irá reconhecer.

>>> lista = [[1,2,3],['a','b','c',3],['a',[3]]]
>>> lista.count(3)
0


###################### .extend() ######################


extend(interavel)
Adiciona objetos no final da lista interando-os.

Um dado interavel é uma sequência que pode ser resultado de uma range() ou
uma outra lista.

>>> lista = [1,2,3,'a','b','c',3,'a',3]
>>> lista.extend(range(1,20))
>>> lista
[1, 2, 3, 'a', 'b', 'c', 3, 'a', 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


>>> lista = [1,2,3,'a','b','c',3,'a',3]
>>> lista.extend([1,1,1,1,1])
>>> lista
[1, 2, 3, 'a', 'b', 'c', 3, 'a', 3, 1, 1, 1, 1, 1]


###################### .insert() ######################

insert(índice,objeto)
Insire o objeto na posição indicada (índice).


>>> lista = [1,2,3,'a','b','c',3,'a',3]
>>> lista.insert(4,'inserção na posição 4')
>>> lista
[1, 2, 3, 'a', 'inserção na posição 4', 'b', 'c', 3, 'a', 3]




###################### .index() ######################


index(valor, inicio=0, fim=2147483647)

Retorna a posição na lista do valor solicitado. 
Pode colocar o numero da posição inicial (inicio) e final (fim) para o 
programa procurar. O programa procura até a posição 2147483647!


>>> lista
[1, 2, 3, 'a', 'inserção na posição 4', 'b', 'c', 3, 'a', 3]
>>> lista.index('b')
5

Agora vamos fazer uma busca em uma posição que o item não está!
>>> lista.index('c',0,5)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    lista.index('c',0,5)
ValueError: 'c' is not in list

Se ele não encontrar o item um erro será retornado para o programa.
Isso acontece até com objetos que não estão na lista exemplo:

>>> lista.index('agua')
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    lista.index('agua')
ValueError: 'agua' is not in list

Note, por mais que a posição do item seja 6, o fim deve ser no minimo uma
posição acima:

>>> lista.index('c',0,6)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    lista.index('c',0,6)
ValueError: 'c' is not in list

Agora fazendo a busca corretamente!

>>> lista.index('c',0,7)
6



###################### .sort() ######################

sort(reverse=True/False)
Ele ordena os valores de menor para maior. Caso o reverse estiver como True
ele irá inverter do maior para menor. Atenção, os dados devem ser todos 
string ou numérico. Não pode haver mistura dos dois tipos na lista a ser ordenada.

>>> lista
[1, 2, 3, 'a', 'inserção na posição 4', 'b', 'c', 3, 'a', 3]
>>> lista.sort()
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    lista.sort()
TypeError: '<' not supported between instances of 'str' and 'int'

Criando uma lista com números randômicos.

>>> lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]

Ordenando a lista!

>>> lista.sort()
>>> lista
[1, 2, 3, 3, 4, 4, 4, 5, 8, 8, 9, 10, 45, 450, 564]

Ordenando a lista reversamente!

>>> lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
>>> lista.sort(reverse=True)
>>> lista
[564, 450, 45, 10, 9, 8, 8, 5, 4, 4, 4, 3, 3, 2, 1]




###################### .reverse() ######################

reverse()

Ele reverte a ordem da lista. Ele não ordena, só altera a posição para a 
posição inversa.

>>> lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
>>> lista.reverse()
>>> lista
[450, 45, 564, 10, 4, 2, 8, 1, 3, 5, 4, 9, 4, 3, 8]
>>> lista.reverse()
>>> lista
[8, 3, 4, 9, 4, 5, 3, 1, 8, 2, 4, 10, 564, 45, 450]


###################### .pop() ######################

pop(indice)

Remove o objeto na posição indicada e retorna o valor removido.
Caso não indique o indice do arquivo o .pop() irá remover o ultimo item 
da lista. 

Note que o .pop() retorna o valor removido. O mesmo pode ser salvo em uma 
variável.

>>> lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
>>> lista.pop()
450
>>> variavel = lista.pop()
>>> variavel
45
>>> lista
[8, 3, 4, 9, 4, 5, 3, 1, 8, 2, 4, 10, 564]

Agora vamos remover o item na terceira posição:

>>> lista.pop(3)
9
>>> lista
[8, 3, 4, 4, 5, 3, 1, 8, 2, 4, 10, 564]



###################### .remove() ######################
remove(valor)
remove a primeira ocorrência do valor digitado.

>>> lista
[8, 3, 4, 4, 5, 3, 1, 8, 2, 4, 10, 564]
>>> lista.remove(3)
>>> lista
[8, 4, 4, 5, 3, 1, 8, 2, 4, 10, 564]
>>> 

Neste caso o item removido não é retornado para o programa.


###################### .clear() ######################

clear()
remove todos os itens da lista

>>> lista
[8, 4, 4, 5, 3, 1, 8, 2, 4, 10, 564]
>>> lista.clear()
>>> lista
[]