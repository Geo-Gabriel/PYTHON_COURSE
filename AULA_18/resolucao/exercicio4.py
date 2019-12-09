# Aula 18 - 03-12-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) 
# O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )

cabe = cerveja[0] 
# ('marca', 'tipo', 'ibu','preço')

dados = cerveja[1:]


# for dados_cerveja in dados:
#     for i in range (4):
#         print(f"{cabe[i]} {dados_cerveja[i]}")
       


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com 
# um dicionários 
# referenciando cada uma destas cervejas.


def recebe(cerveja):
    cabe = cerveja[0] # Separar o cabeçalho da tuplua
    dados = cerveja[1:] # Separar os dados da tupla
    lista_cerva = [] # Iniciar uma lista para receber os dados
    for dados_cerveja in dados: # For para quebrar os dados
        # Gerando o dicionário para armazenar os dados
        dicionario = {cabe[0]:dados_cerveja[0],cabe[1]:dados_cerveja[1],
                      cabe[2]:dados_cerveja[2],cabe[3]:dados_cerveja[3]}

        lista_cerva.append(dicionario) # Adicionando o dicionario na lista
    return lista_cerva #Retornando a lista para o programa.

print(recebe(cerveja))
[
 {'marca': 'Skol', 'tipo': 'IPA', 'ibu': 'ultra-leve', 'preço': 3.5},
 {'marca': 'Brahma', 'tipo': 'lager', 'ibu': 'leve/media', 'preço': 3.45},
 {'marca': 'Kaiser', 'tipo': 'Americam Larger', 'ibu': 'leve', 'preço': 2.35}, 
 {'marca': 'Sol', 'tipo': 'larger mão', 'ibu': 'agua', 'preço': 1.19}
 ]