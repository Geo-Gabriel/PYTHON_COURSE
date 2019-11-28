# nome marca teor tipo cerveja


def save_beer(beer):
    arq = open('beer.txt', 'a')
    arq.write(f"{beer['nome']};{beer['marca']};{beer['teor']};{beer['tipo']}\n")
    arq.close()

def ler_cerveja():
    lista_beer = []
    arq = ('beer.txt', 'r')
    for linha in arq:
        linha = linha.split()
        linha_cerv = linha.strip(';')
        cerveja = {'nome': linha_cerv[0], 'marca': linha_cerv[1], 'teor': linha_cerv[2], 'tipo': linha_cerv[3]}
        lista_beer.append(cerveja)

    arq.close()
    return lista_beer


# nome_beer = input('Digite nome da cerveja: ')
# marca = input('Digite a marca: ')
# teor_alc = int(input('Digite o teor de álcool: '))
# tipo = input('Digite o tipo da cerveja: ')
# cerveja = {'nome': nome_beer, 'marca': marca, 'teor': teor_alc, 'tipo': tipo}

# save_beer(dicio_beer)



for bebidas in ler_cerveja():
    print(f"{bebidas['nome']} - {bebidas['marca']} - {bebidas['teor']} - {bebidas['tipo']}")