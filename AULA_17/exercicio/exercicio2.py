# 1 - Faça um menu interativo que tenha: Cadastro da banda, cadastro 
# do album, cadastro da musica, Sair.
# O menu deve ser executado até que se escolha a opção sair.
# Cada opção deve ser mostrada 
# quando selecionado a opção sair, deverá aparecer na tela as 
# informações das banda cadastradas, 
# albuns e musicas.

lista_banda = []
lista_album = []
lista_musica = []

menu = '''
#############################################################################
                             Cadastro Faixas
#############################################################################

1 - Cadastro banda
2 - Cadastro album
3 - Cadastro musica
4 - sair

Digite a opção: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        lista_banda.append(input('Digite o nome da banda: '))
    elif opcao == '2':
        lista_album.append(input('Digite o nome da album: '))
    elif opcao == '3':
        lista_musica.append(input('Digite o nome da musica: '))
    elif opcao == '4':
        print(f'lista de banda: {lista_banda}\nlista de album: {lista_album}\nlista de musica: {lista_musica}')
        break
    else:
        print('opção invalida')



    




