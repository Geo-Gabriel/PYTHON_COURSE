# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]



# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com dicionario.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#


def lista (lista):
        lista = []
        for n in lista:
                dicio = {'codigo': n,'produto': n,'valor':n,'quantidade': n}
                lista.append(dicio)
        return lista

print(lista(lista))



def lista(lista):
        lista = []
        for n in range(len(lista[0])):
                dicio = {}
                for i in range(len(lista)):
                        dicio[lista[i]] = lista[i][n]
                        lista.append(dicio)
        return lista

print(lista(lista))