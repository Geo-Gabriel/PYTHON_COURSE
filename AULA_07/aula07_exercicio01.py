# EXERCICIO 01 -- DICIONÁRIO
# Escreva um programa que leia os dados da cerveja
# Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume (ml)
# Crie um dicionário que armazene os dados
# Imprima os dados do dicionario (nao dicionario completo)

# DICIONÁRIO PODE SER DINÂMICO - POSSO INSERIR E ALTERAR VALORES A QUALQUER INSTANTE. 


inf_cerveja = {"marca": input('Digite a marca da cerveja: '), "tipo": input('Digite tipo: '), 'ibu': input('Digite IBU (International Bitterness Unitis): '), 'abv': input('Digite ABV (Alcohol by volume): '), 'EBC': input('Digite EBC (European Brewing Convention): '), 'volume':input('Digite volume em (ml): ')}

print('=-='*15)
print(f'A marca é: {inf_cerveja["marca"]}\nO tipo é: {inf_cerveja["tipo"]}\nO IBU é: {inf_cerveja["ibu"]}\nO ABV é: {inf_cerveja["abv"]}\nO EBC é: {inf_cerveja["abv"]}\nO volume é: {inf_cerveja["volume"]} ml')
print('=-='*15)


# ALTERNATIVA

# -- Criar variáveis e depois inserir estas variáveis no dicionário ['chave': (variavel criada)]

#  ALTERNATIVA II

# -- Criar um dicionário vazio depois criar chaves com valores definidos pelo INPUT. Estas chaves criadas serão adicionadas
# -- ao dicionário. 