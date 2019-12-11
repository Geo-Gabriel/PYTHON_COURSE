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
    def __init__(self, dado_bruto1): # Aqui vai receber como parametro a variavel dadobruto


                                        # Aqui sera os atributos de variáveis
        self.dado_bruto = dado_bruto1
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def listar(self):  ##  Aqui é o método que vai adicionar o dado bruto nas variáveis

        lista = self.dado_bruto.strip().split(';')
        self.codigo = int(lista[0])
        self.nome = (lista[1])
        self.idade = int(lista[2])
        self.sexo = lista[3]
        self.email = lista[4]
        self.telefone = lista[5]

    def salvar (self, dadobrutus):
        arquivo_clientes = open('Arq_cliente.txt', 'w')
        arquivo_clientes.write(dadobrutus)
        arquivo_clientes.close()


a = Cliente(dadobruto) # Aqui estou salvando a minha classe em uma variável 'a'

a.listar() # aqui estou chamando o método (listar)
a.salvar(dadobruto)

                                                #Aqui eu imprimo os dados 

print(f' Codigo: {a.codigo} \n Nome: {a.nome} \n Idade: {a.idade} \n Sexo: {a.sexo} \n Email: {a.email} \n Telefone: {a.telefone}')

