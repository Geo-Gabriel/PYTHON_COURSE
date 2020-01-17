# Criar um programa para o cadastro de clientes
# para o cadastro deve pedir os seguintes dados: 
# Codigo do cliente, CPF, Nome completo, D. nascimento
# Estado, Cidade, CEP, Bairro, rua, nº casa, complemento

# Trabalhando com varios dados

# cod_Cliente = input('Codigo de cliente: ')

def cadastro_cliente (numero_funcao):
    dados_Cliente = ['codigo_cliente', 'cpf', 'nome_completo', 'data_nascimento', 'estado', 'cidade', 'cep', 'bairro', 'rua', 'num_casa', 'complemento']
    lista = []


    for j in range(numero_funcao): 
        dicionario = {} #Para cada cliente será criado um novo dicionário com os dados_cliente

        for i in dados_Cliente: #economizar inputs com o FOR
            dicionario[i] = input(f'{i} : ') # para cada dados na lista dados_cliente será a chave do dicionário e o input será o valor a ser atribuído em relaçao a chave
        lista.append(dicionario) # Aqui vai adicionar o dicionário na lista
            #lista.append(input(f'{i}: ')) # O laço vai interagir com cada elemento contido em dados_cliente.
        
    return lista


numero = int(input('Digite quantos cadastros irá fazer: '))

lista_cadastro = cadastro_cliente(numero)

# Criar uma função para salvar em arquivo: 

arq = open('clientes.txt', 'a')
for cliente in arq:
        cliente_chave = list(cliente.keys)
    for chaves in cliente:
        salvar = f'{cliente['codigo_cliente']}'
arq.write(cadastro_cliente)

arq.close()
