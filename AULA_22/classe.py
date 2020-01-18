# 1) O que uma pessoa Tem? Quais as caracteristicas? 

# 2) O que uma pessoa faz? 

# 3) Como a pessoa está agora? 


#(atributos, metodos, atributos estado)

class Pessoa:
    ''' 
    Classe demonstrativo para compreensão de como 
    montar uma classe pessoa
    '''
    def __init__ (self,nome1,cpf1,data_de_nascimento1,altura1,salario1,endereço1):
        ''' 
        __init__ é o construtor da classe. Ela é responsável por
        inicializar as variáveis importantes para poder trabalhar 0com classe.
        '''
        ################################ Atributos
        self.nome = nome1
        self.cpf = cpf1
        self.data_de_nascimento = data_de_nascimento1
        self.altura = altura1
        self.salario = salario1
        self.endereço = endereço1
        ############################### Atributos de estado
        # Estado da pessoa
        self.fome = None
        self.sede = None
        self.exausta = None

    
    def correr(self,distancia):
        '''
        Adicione a distância em metros percorrida
        '''
        if distancia <= 50:
            self.exausta = 'não'
        elif distancia > 50 and distancia < 200:
            self.exausta = 'levemente exausta'
            self.sede = 'pouca'
            self.fomr = 'pouca'
        else:
            self.exausta = 'exausta'
            self.sede = 'muita'
            self.fome = 'muita'
        

    def beber(self,litro):
        '''
        Metodo para melhorar o status de sede
        '''
        if litro > 0.5 and litro < 1:
            if self.sede == None or 'não':
                self.sede = 'não'
            elif self.sede == 'pouca':
                self.sede = 'não'
            elif self.sede == 'muita':
                self.sede = 'pouca'
        elif litro >= 1:
            if self.sede == None or 'não':
                self.sede = 'não'
            elif self.sede == 'pouca':
                self.sede = 'não'
            elif self.sede == 'muita':
                self.sede = 'não'

    def comer(self):
        self.fome = 'não'

    def descansar(self,tempo):
        if tempo < 5:
            if self.exausta == None or 'não':
                self.exausta = 'não'
            elif self.exausta == 'levemente exausta':
                self.exausta = 'não'
            elif self.exausta == 'exausta':
                self.exausta = 'levemente exausta'
        elif tempo >=5 :
            if self.exausta == None or 'não':
                self.exausta = 'não'
            elif self.exausta == 'levemente exausta':
                self.exausta = 'não'
            elif self.exausta == 'exausta':
                self.exausta = 'não'

    def jantar_noitesono(self):
        self.exausta = 'não'
        self.fome = 'não'
        self.sede = 'não'


### Exemplo de uso de classe...

pessoa1 = Pessoa('Alberto','04304304322','22/06/2001',198,1500.00,'R. Itapé, 20')


# print(f'Exausta: {pessoa1.exausta}')
# print(f'Sede: {pessoa1.sede}')
# print(f'fome: {pessoa1.fome}')


pessoa1.correr(300)

print(f'Exausta: {pessoa1.exausta}')
print(f'Sede: {pessoa1.sede}')
print(f'fome: {pessoa1.fome}')

#pessoa1.beber(1)

# print(f'Exausta: {pessoa1.exausta}')
# print(f'Sede: {pessoa1.sede}')
# print(f'fome: {pessoa1.fome}')

#pessoa1.comer()

# print('\n')
# print(f'Exausta: {pessoa1.exausta}')
# print(f'Sede: {pessoa1.sede}')
# print(f'fome: {pessoa1.fome}')

#pessoa1.descansar(4)
pessoa1.jantar_noitesono()

print('\n')
print(f'Exausta: {pessoa1.exausta}')
print(f'Sede: {pessoa1.sede}')
print(f'fome: {pessoa1.fome}')