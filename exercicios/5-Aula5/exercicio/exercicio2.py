# 2 -
# Mercado Tech ----
# Solicitar Nome do funcionario
# Solicitar idade
# Informar se o funcionario pode adquirir produtos alcoolicos

#3 -
# Cadastro Produtos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolicos e Não Alcoolicos)
# Exibir o produto cadastrado
nome=str(input('Digite o nome do funcionário: '))
idade=int(input('Digite a idade do funcionário: '))

if idade>=18:
    print(f'O funcionário {nome} pode comprar bebidas.')
else:
    print(f'O funcionário {nome} não pode comprar bebidas')    