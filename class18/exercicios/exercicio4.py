# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

tupla_de_cervejas = (
    ('marca', 'tipo', 'ibu','preço'),
    ('Skol','IPA','ultra-leve',3.50),
    ('Brahma','lager','leve/media',3.45),
    ('Kaiser','Americam L','leve',2.35),
    ('Sol','larger mão','agua',1.19)
)


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.


for i in tupla_de_cervejas:
    print(f'{i[0]} \t{i[1]} \t {i[2]} \t {i[3]}')


# def dic_cerveja (cervejas):
#     lista = []
#     for i in range(1,5):

#         dicio = {'marca': cervejas[i][0] , 'tipo':cervejas[i][1], 'ibu':cervejas[i][2], 'preco':cervejas[i][3]}
#         lista.append(dicio)
#     return lista

def dic_cerveja (cervejas):
    lista = []
    tupla_sem_campos = cervejas[1:]
    for cerveja in tupla_sem_campos:

        dicio = {'marca': cerveja[0] , 'tipo':cerveja[1], 'ibu':cerveja[2], 'preco':cerveja[3]}
        lista.append(dicio)
    return lista

print(dic_cerveja(tupla_de_cervejas))