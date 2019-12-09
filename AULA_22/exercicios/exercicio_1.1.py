# --- Aula 22 -- 09/12/2019

# Crie uma classe cliente

# deve ter como atributos: codigo, cpf, nome, idade, sexo

# como metodos: receber salario, comprar, pagar divida

# quando recebe aumenta o dinheiro na carteira.
# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e nao tiver dinheiro o suficiente deve diminuir o dinheiro da carteira e aumentar a divida
# para pagar a divida tem que ter dinheiro o suficiente na carteira

# -- 03) atributos de estado: dinheiro na carteira, divida, bens 


class Cliente:
    '''
    Esta classe é o estado de um cliente
    
    '''
        ###################################### atributos variáveis

    def __init__(self, nome1, codigo1, cpf1, idade1, sexo1): 

        ######################################## atributos
        self.nome = nome1
        self.codigo = codigo1
        self.cpf = cpf1
        self.idade = idade1
        self.sexo = sexo1

        ####################################### atributos de estado
        self.carteira = 0
        self.bens = None 

        #############################################################

    def receber_salario (self, trabalhou):
        if trabalhou > 0:
            self.carteira = trabalhou

    def comprar (self, bens, gastar):
        self.bens = bens
        print(f'Você adquiriu: {bens}')
        self.carteira -= gastar
    
    def pagar_divida (self):
        if self.carteira >= 5000:
            self. carteira -= 2580
            print('Pagou divida de 2580')
        else:
            print('Não foi possivel pagar a divida')


cliente1 = Cliente('George', '02', '8004452844588', 18, 'M',)

cliente1.receber_salario(int(input('Digite o valor a receber: ')))
print(f'Você tem esse valor na carteira: {cliente1.carteira}')

cliente1.comprar((input('Digite o que vai comprar: ')),(int(input('Digite o valor: '))))
print(f'Novo saldo: {cliente1.carteira}')


cliente1.pagar_divida()
print(f'Saldo restante: {cliente1.carteira}')