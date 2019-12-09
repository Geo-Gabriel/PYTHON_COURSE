def criar_faixa (musica, album, artista):
    # Cria uma variável que contém um dicionário com os dados
    faixa = {'musica':musica, 'album': album, 'artista': artista}
    return faixa # Me retorna o dicionário criado

def salvar_faixa(faixa):
    # Insere o caminho da pasta onde ira ser salvo as faixas
    arq = open('class16/faixas.txt', 'a')
    # aqui escreve os dados no arquivo 'faixas.txt'
    arq.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']};\n")
    # Aqui fecha o arquivo
    arq.close()

def ler_faixas ():
    arq = open('class16/faixas.txt', 'r')
    lista_faixas = []
    for linha in arq:
        linha = linha.strip() # Retira as quebras de linhas
        dados_faixa = linha.split(';') # Quando encontrar o ponto e virgula vai separar as strings
        # Chama o método que cria o dicionário. com as respectivas posições. A variável faixa é do tipo dict
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2])
        lista_faixas.append(faixa)
    arq.close()
    return lista_faixas # Retorna minha lista que tem as faixas
    