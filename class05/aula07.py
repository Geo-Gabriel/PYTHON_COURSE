# FORMA 01

user = int(input('Digite 01 para cadastrar produto ou 2 para sair: '))

lista_alcoolica = []
lista_n_alcoolica = []
while user != 2:
    op = int(input('Digite 3 se o produto é alcoolico ou 4 para n/alcoolico: '))
    x = input('Digite o nome do produto: ')

    if op == 3:
        lista_alcoolica.append(x)
    else:
        lista_n_alcoolica.append(x)

    user = int(input('Digite 01 para cadastrar mais produto ou 2 para sair: '))

print('A lista alcoolica é: ', lista_alcoolica)
print('A lista n alcoolica é: ', lista_n_alcoolica)

# FORMA 02

'''nome_produto = input('Digite o nome do produto: ')

categoria_produto = int(input('Digite 01 para alcoolico ou 2 para nao alcoolico: '))

if categoria_produto == 1:
    print('O produto é {} e ele não é alcoolico'.format(nome_produto))
elif categoria_produto == 2:
    print('O produto é {} e ele não é alcoolico'.format(nome_produto))
else:
    print('categoria n existe')'''