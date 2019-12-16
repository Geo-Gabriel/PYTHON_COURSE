import random
 

def lista_simples_int_str(numero_objetos = int(random.randint(5,100))):
    '''
    Retorna lista randômica, pura, composta de string ou inteiros, variando de 5 a 100 itens.

    '''
    tipo_lista = int(random.randint(0,1))
    if tipo_lista == 0:
        lista = lista_simples_str(numero_objetos)
    else:
        lista = lista_simples_int(numero_objetos)
    return lista

def lista_simples_inpura_int_str(numero_objetos = int(random.randint(5,100))):
    '''
    Retorna lista randômica, impura, composta de string, inteiros ou alfanúmerica, variando de 5 a 100 itens.

    '''
    tipo_lista = int(random.randint(0,2))
    if tipo_lista == 0:
        lista = lista_simples_str(numero_objetos)
    elif tipo_lista == 1:
        lista = lista_simples_impura(numero_objetos)
    else:
        lista = lista_simples_int(numero_objetos)
    return lista


def lista_simples_int(numero_objetos = int(random.randint(5,100))):
    '''
    Retorna uma lista randômica com inteiros contendo de 5 a 100 itens.
    '''
    lista = []
    for i in range(numero_objetos):
        lista.append(int(random.randint(1,1000)))
    return lista

def lista_simples_str(numero_objetos = int(random.randint(5,100))):
    '''
    Retorna uma lista randômica com string, de 1 a 10 caracteres, contendo de 5 a 100 itens.
    Os caracteres podem ser minusculos ou maiusculos.
    '''
    lista_alfabetica = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                        'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'o', 'p', 'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z']
    lista = []
    for i in range(numero_objetos):
        letra = ''
        for i in range(int(random.randint(1,10))):
            char = random.choice(lista_alfabetica)
            if int(random.randint(0,1)) == 1:
                letra = letra + char.upper()
            else:
                letra = letra + char
        lista.append(letra)
    return lista

def lista_simples_impura(numero_objetos = int(random.randint(5,100))):
    '''
    Retorna uma lista randômica com alfanumérica, de 1 a 10 caracteres, numeros de 0 a 1000,
    contendo de 5 a 100 itens.
    Os caracteres podem ser minusculos ou maiusculos.
    '''
    lista_alfabetica = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                        'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'o', 'p', 'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z', '0', '1',
                        '2', '3', '4', '5', '6', '7', '8',
                        '9']
    lista = []
    for i in range(numero_objetos):
        letra = ''
        if int(random.randint(0,1)) == 0:
            lista.append(random.randint(0,1000))
        else:
            for i in range(int(random.randint(1,10))):
                char = random.choice(lista_alfabetica)
                if int(random.randint(0,1)) == 0:
                    letra = letra + char.upper()
                else: 
                    letra = letra + char
            lista.append(letra)
    return lista

            
def lista_lista_int():
    pass


def embaralhar(numero=3,numero_objetos=30,lista_return=None):
    '''
    Cria uma lista contendo várias listas, inteiras com 30 itens. Ela irá copiar estas listas e 
    embaralhar de forma que não se sabe se as listas são as mesmas ou são somente iguais!
    '''
    lista = []
    lista1 = []
    lista2 = []
    for i in range(numero):
        lista1.append(lista_simples_int(numero_objetos))

    for i in lista1:
        lista2.append(i.copy())
    lista1.extend(lista2)
    # quntas listas deve ser retornadas!
    if lista_return == None:
        for i in lista1:
            lista.append(random.choice(lista1))
    else:
        for i in range(lista_return):
            lista.append(random.choice(lista1))
    
    return lista


def embaralhar_int_str_hard(numero=3,numero_objetos=30):
    '''
    Cria uma lista contendo várias listas, inteiras, string ou alfanunéricas com vários itens.
    Ela irá copiar estas listas e embaralhar de forma que não se sabe se as listas são as mesmas 
    ou são somente iguais!
    '''
    lista = []
    lista1 = []
    lista2 = []
    for i in range(numero):
        lista1.append(lista_simples_inpura_int_str(numero_objetos))

    for i in lista1:
        lista2.append(i.copy())
    lista1.extend(lista2)
    multiplicador = random.randint(1,25)
    for i in range(len(lista1) * multiplicador):
        lista.append(random.choice(lista1))
    
    return lista


def binario (numero_objetos=8):
    lista = []
    for i in range(numero_objetos):
        lista.append(random.randint(0,1))
    return lista