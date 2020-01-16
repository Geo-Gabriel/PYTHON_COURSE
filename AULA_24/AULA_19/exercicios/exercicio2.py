# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)

# def dados (pessoa):
#         lista = []
#         for p in range (0,7):
#                 dicio = {'nome': pessoa[0][p], 'tel': pessoa[1][p], 'mail': pessoa[2][p], 'idade': pessoa[3][p]}
#                 if int(dicio['idade']) >= 18:
#                         lista.append(dicio)         
#         return lista


def dados(pessoa):
        lista = []
        for n in range(len(pess[0])):
                dicio = {}
                for i in range(len(cab)):
                        dicio[cab[i]] = pessoa[i][n]
                if int(dicio['idade']) >= 18:
                        lista.append(dicio)
        return lista

# dados_pessoas = dados(pess)

print(dados(pess))

# print() #AQUI FEZ UMA QUEBRA DE LINHA

# for dados in dados(pess):
#         print(dados)

# print()

# for paa in dados_pessoas:
#         print(f'{paa}')