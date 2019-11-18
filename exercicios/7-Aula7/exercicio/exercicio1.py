#--- Exercício 1 - Dicionario
#--- Escreva um programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#--- Crie um dicionario para armazenar os dados
#--- Imprima os dados do dicionário (não dicionário completo)

#--- Correção 1 ---#
# Resolvido por: Gabriel Rodrigo Parasky <3

marca = input('Informe a marca\n')
tipo = input('Informe o tipo\n')
ibu = input('Informe o IBU\n')
abv = input('Informe o ABV\n')
ebc = input('Informe o EBC\n')
volume = input('Informe o volume\n')

inf_cerveja = {'Marca':marca , 'Tipo':tipo , 'IBU':ibu , 'ABV':abv , 'EBC':ebc , 'Volume':volume}
print(f"{inf_cerveja['Marca']} | {inf_cerveja['Tipo']} | {inf_cerveja['IBU']} | {inf_cerveja['ABV']} | {inf_cerveja['EBC']} | {inf_cerveja['Volume']}")

#--- Correção 2 ---#
#--- Resolvido por Gustavo Antunes Voltolini
cerveja = {}
cerveja ['Marca'] = (input('Digite a marca: '))
cerveja ['Tipo'] = (input('Digite o tipo: '))
cerveja ['IBU'] = int(input('Digite o IBU(inteiros): '))
cerveja ['ABV'] = float(input('Digite o ABV(inteiros): '))
cerveja ['EBC'] = float(input('Digite o EBC: '))
cerveja ['volume'] = float(input('Digite o volume: '))

print (f"Marca{cerveja['Marca']} - Tipo: {cerveja['Tipo']} - IBU: {cerveja['IBU']} - ABV: {cerveja['ABV']} - EBC: {cerveja['EBC']} - Volume: {cerveja['volume']}")
