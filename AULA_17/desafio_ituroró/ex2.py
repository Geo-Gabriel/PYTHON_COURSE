# 1 - Faça um menu interativo que tenha: Cadastro de bandas, cadastro de músicas, cadastro de album e sair.
# O menu deve ser executado até que se escolha a opção sair.
# Quando selecionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas, albuns e musicas. 

menu = ''' 
==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==
#                                    MUSIC UNIVERSE V 1.0.0                                     #
==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==---==

1...>> Cadastro de Bandas
2...>> Cadastro de Músicas
3...>> Cadastro de Álbum
4...>> Sair

Digite a opção....  '''

# 

bandas = []
musicas = []
album = []

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Bandas')
        a = input('Digite o nome da banda: ')
        bandas.append(a)
        print('Banda cadastrada com sucesso!')

    elif opcao == '2':
        print('Cadastro de Músicas')
        b = input('Digite o nome da música: ')
        musicas.append(b)
        print('Música cadastrada com sucesso!')

    elif opcao == '3':
        print('Cadastro de Álbum')
        c = input('Digite o nome do álbum: ')
        album.append(c)
        print('Álbum cadastrada com sucesso!')

    elif opcao == '4':
        print('Sair')
        break
    else:
        print('Opção inválida')
        

print(f'Músicas cadastradas:.>> {musicas}')
print(f'Bandas cadastradas:.>> {bandas}')
print(f'Álbums cadastrados:.>> {album}')
