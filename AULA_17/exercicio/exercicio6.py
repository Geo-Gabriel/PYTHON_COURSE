# Criar um programa para o cadastro do cliente
# Para cadastro de clientes deve pedir os seguintes dados: 
# Codigo do cliente, CPF, Nome completo, 
# data de nascimento, Estado, Cidade, cep, bairro, rua, 
# numero da casa, complemento.

# cod_Cliente = input('Codigo de cliente: ')
# cpf = input('CPF cliente: ')


def cadastro_cliente(numero_funcao):
    dados_cliente = ['Codigo_cliente', 'CPF', 'nome_completo', 
                    'data_de_nascimento', 'estado', 'cidade',
                    'cep', 'bairro', 'rua', 'numero_casa', 'complemento']
    lista=[]
    for j in range(numero_funcao):
        dicionario = {}

        for i in dados_cliente:
            dicionario[i]= input(f'{i}: ')
        
        lista.append(dicionario)
    return lista

#numero=int(input('Digite numero de  cadastros: '))
#lista_cadastro = cadastro_cliente(numero)


lista_cadastro = [{'Codigo_cliente':12, 'CPF':00000, 'nome_completo':'Alberto', 
                    'data_de_nascimento':"10/12/2000", 'estado':'SC',
                    'cidade':'Camboriú',
                    'cep':8885555, 'bairro':Garcia, 'rua':'Italia',
                    'numero_casa':53, 'complemento': 'ap 35'}]
# Criar uma função para salvar em arquivo:

for cliente in lista_cadastro:
    cliente_chave = list(cliente.keys())
    for chaves in cliente_chave:
        salva = (f'{cliente[chaves]}')
        print(salva)


# Continua em outra hora


