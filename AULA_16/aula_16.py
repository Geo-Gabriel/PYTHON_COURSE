# Aula 16 ----- 29-11-2019

# Importa os métodos que estão em outro arquivo

from faixa import criar_faixa, salvar_faixa, ler_faixas

# Cadastro de playlist
# Lendo musica, artista, e album

# Inputs p/ inserir os dados da faixa

musica = input('Digite uma musica: ')
artista = input('Digite artista: ')
album = input('Digite album: ')

# Aqui está chamando os métodos que estão no arquivo AULA_16/metodos_faixa.py 

faixa = criar_faixa(musica, artista, album)
salvar_faixa(faixa)
lista = ler_faixas()

# Percorre todos os elementos na lista com o laço FOR e imprime

for f in lista: # 'f' se refere as faixas contidas na lista p/ faixas na lista
    print(f"{f['musica']} - {f['artista']} - {f['album']}")
