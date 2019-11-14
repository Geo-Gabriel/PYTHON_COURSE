# EXERCICIO 02 - DICIONARIOS
# Escreva um programa que leia os dados de 11 jogadores
# Jogador: Nome, Posicao, Numero, pernaboa
# Crie um dicionario para armazenar os dados
# imprima os dados do dicionario (n dicionario completo)
# Imprima todos os jogadores e seus dados



lista_jogadores = list()

n = 1

for i in range (1,3):
    dados_jogadores = dict()
    dados_jogadores['nome'] = input(f'Digite o nome do jogador {n}: ')
    dados_jogadores['posicao'] = input('Digite posição: ')
    dados_jogadores['numero'] = int(input('Digite numero: '))
    dados_jogadores['pernaboa'] = input('tem perna boa?: ')
    print()
    lista_jogadores.append(dados_jogadores)
    n = n + 1
       
s = 1  

for dados in lista_jogadores:
    print('=-='*30)
    print(f" Jogador {s} ---  Nome: {dados['nome']} || Posição: {dados['posicao']} || Número: {dados['numero']} || Perna boa?: {dados['pernaboa']}")
    print('=-='*30)
    print()
    print()
    s = s + 1