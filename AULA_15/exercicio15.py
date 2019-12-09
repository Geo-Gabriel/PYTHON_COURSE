# nome marca teor tipo cerveja


def save_beer(cerveja_dicio):
    arq = open('beer.txt', 'a')
    arq.write(f"{cerveja_dicio['nome']};{cerveja_dicio['marca']};{cerveja_dicio['teor']};{cerveja_dicio['tipo']}\n")
    arq.close()

def ler_cerveja():
    lista_beer = []
    arq = open('beer.txt', 'r')
    for linha in arq:
        linha = linha.strip()
        linha_linha = linha.split(';')
        cerveja = {'nome': linha_linha[0], 'marca': linha_linha[1], 'teor': linha_linha[2], 'tipo': linha_linha[3]}
        lista_beer.append(cerveja)
    arq.close()
    return lista_beer


# nome_beer = input('Digite nome da cerveja: ')
# marca = input('Digite a marca: ')
# teor_alc = int(input('Digite o teor de álcool: '))
# tipo = input('Digite o tipo da cerveja: ')
# cerveja = {'nome': nome_beer, 'marca': marca, 'teor': teor_alc, 'tipo': tipo}

# save_beer(cerveja)

lista = ler_cerveja()
for p in ler_cerveja():
    print(f"{p['nome']} - {p['marca']} - {p['teor']} - {p['tipo']}")