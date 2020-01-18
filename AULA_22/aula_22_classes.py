# 1-- O que uma pessoa tem? Quais as caracteristicas?
############ AQUI ESTÁ RELACIONADO A ATRIBUTOS QUE PODEM SER CONVERTIDOS EM VARIÁVEIS #################
# nome
# idade
# telefone
# sexo
# endereço


# 2-- O que uma pessoas faz?
################ MÉTODOS(FUNÇÃO/PROCRDIMENTO) PARADIGMA PROCEDURAL --  
# come
# dorme
# bebe
# namora
# reproduz
# trabalha
# estuda

# 3-- Como a pessoa está agora?
###################### ATRIBUTOS DE ESTADO -- PODEM MUDAR -- VARIÁVEIS ############

# viva
# cansada
# ansiosa
# com fome
# com sede
# com dor no corpo
  

##############------------############################### -------------- ########################------------##########



# # 1) O que uma pessoa Tem? Quais as caracteristicas? 
# ####### Atributos  ---- variáveis
# nome 
# idade
# telefone
# sexo

# # 2) O que uma pessoa faz? 
# # metodos  (função/procedimento)
# respira
# dorme
# corre
# bebe
# come
# multiplica ####


# # 3) Como a pessoa está agora? 
# # Atributos de estado - Variáveis
# divida
# cansada
# viva
# fome
# sede


class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__ (self,nome1, idade1, telefone1, sexo1):
        ''' 
        O __init__ é o motor que irá iniciar as variáveis da clase
        O self é o que irá conecta toda a classe
        '''
        # Atributos ##########
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        # 
        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    #### Metodos

    def respira (self,respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False

    def corre (self,distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'

    def dorme (self):
        if self.viva:
            self.cansada = 'não'
            self.bebe()
            self.come()


    def bebe (self):
        if self.viva:
                self.sede = 'não'
    
    def come (self):
        if self.viva:
            self.fome = 'não'
        

    def multiplica (self):
        pass # para outra hora!




p = Pessoa('Antonio',18,'479966995','m')

# p.respira(False)

# p.respira(True)

p.corre(300)
p.dorme()
# p.come()
# p.bebe()
print(f'Nome é {p.nome}')
print(f'Está vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f'Está com sede? {p.sede}')
print(f'Está cansada {p.cansada}')
