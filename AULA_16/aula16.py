# aula 16 ----- 29-11-2019
#??


# importa os métodos que estão em outro arquivo
from faixa import criar_faixa, salvar_faixa, ler_faixas




#cadastro de playlist
#lendo musica, artista, e album

# Inputs p/ inserir os dados da faixa

musica = input('Digite uma musica: ')
artista = input('Digite artista: ')
album = input('Digite album: ')

# Aqui está chamando os métodos 

faixa = criar_faixa(musica, artista, album)
salvar_faixa(faixa)
lista = ler_faixas()

for f in lista: # 'f' se refere as faixas contidas na lista p/ faixas na lista
    print(f"{f['musica']} - {f['artista']} - {f['album']}")
