class Pessoa:  #--- Criação da classe (Pessoa)
     '''Classe para utilização no banco de dados'''
    id = 0    #-- Aqui vai os elementos da classe
    nome = ''
    sobrenome = ''
    idade = 0
    endereco_id = 0
    
def exportar_arq (self, lista_pessoas): # -- Aqui exporta os dados para um arquivo em txt
    with open('AULA_35/pesssoas.txt', 'a') as arquivo:
        for p in lista_pessoas: # -- Aqui percorre a lista de dicionarios e salva no arquivo em formato definido
            arquivo.write(f"{str(p)} \n")
            
def __str__(self):
    return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_id}'