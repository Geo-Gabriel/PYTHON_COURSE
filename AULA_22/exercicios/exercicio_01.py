# Aula 21 - 09-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117' # Esta é a variável que a função vai receber


# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto numa variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente:  ## Aqui estou criando a classe 
    '''
    Classe cliente, exercicios sobre classes em python.
    '''
    def __init__(self, dado_bruto1): # RECEBE COMO PARÂMETRO A VARIÁVEL 'dadobruto'


        # ATRIBUTOS DAS VARIÁVEIS

        self.dado_bruto = dado_bruto1
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    # ESTE MÉTODO VAI TRATAR 'dadobruto' E ADD OS DADOS NOS ATRIBUTOS

    def listar(self): 

        lista = self.dado_bruto.strip().split(';')
        self.codigo = int(lista[0])
        self.nome = (lista[1])
        self.idade = int(lista[2])
        self.sexo = lista[3]
        self.email = lista[4]
        self.telefone = lista[5]

    # METODO SALVAR -- SALVA OS DADOS EM UM ARQUIVO

    def salvar (self,nome, atributo = 'a='):
        arquivo_clientes = open('Arq_cliente.txt', atributo)
        texto = f'{self.dado_bruto}\n'
        arquivo_clientes.write(texto)
        arquivo_clientes.close()

    # OU .... 

    def salvar(self,nome, atributo):
        if atributo == 'a':
            arquivo = open('Arq_cliente.txt', atributo)
            texto = f'{self.dado_bruto}\n'
            arquivo.write(texto)
            arquivo.close()
        elif atributo == 'r':
            arquivo = open('Arq_cliente.txt', atributo)
            pass

    # MÉTODO ATUALIZAR DADOS DO CLIENTE

    def atualizar (self):
        # self.codigo = int(input('Digite o código do cliente: ')) -- CÓDIGO NÃO SE ATUALIZA
        self.nome = input('Digite o nome do cliente: ')
        self.idade = int(input('Digite a idade do cliente: '))
        self.sexo = input('Digite o sexo do cliente (F) ou (M): ')
        self.email = input('Digite o email no cliente: ')
        self.telefone = input('Digite o telefone do cliente: ')
        self.dado_bruto = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}'
        self.salvar('arquivo_novo', 'w')



a = Cliente(dadobruto) # Aqui estou salvando a minha classe em uma variável 'a'

a.listar() # aqui estou chamando o método (listar)

a.salvar() #chamando o método salvar

                                                #Aqui eu imprimo os dados 

print(f' Codigo: {a.codigo} \n Nome: {a.nome} \n Idade: {a.idade} \n Sexo: {a.sexo} \n Email: {a.email} \n Telefone: {a.telefone}')

