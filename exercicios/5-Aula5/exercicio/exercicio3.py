#3 -
# Cadastro Produtos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolicos e Não Alcoolicos)
# Exibir o produto cadastrado

nomep= input('Digite o nome do produto')
categoria = int(input('Informe a categoria do produto 1-Alcoolico e 2-Não Alcoolico'))

if categoria ==1:
    print(f'O nome do produto é {nomep} e ele é Alcoolico')
elif categoria ==2:
    print(f'O nome do produto é {nomep} e ele é Não Alcoolico')
else:
    print('Categoria não existe')