#--- Exercício 5 - Funções - 2
#--- Crie uma função que valida um menu
#--- A função deve receber um número inteiro
#--- A função deve checar se o número está entre 0 e 2
#--- Caso o número esteja fora deste range deve ser informado 'Opção inválida'
#--- Caso o número informado esteja dentro do range deve seguir as seguintes regras:
#---    0-Chamar uma função Sair(), esta função deve imprimir 'Usuário realizou o logoff'
#---    1-Chamar uma função Cadastrar(), esta função deve imprimir 'Cadastro de usuários'
#---    2-Chamar uma função Listar(), esta função deve imprimir 'Lista de usuários cadastrados'
#--- Crie um menu com cabeçalho e rodapé com as opções listadas acima
#--- Realize a leitura da opção digitada pelo usuário no terminal
#--- Realize a chamada da função que valida o menu e passe o variável criada durante a leitura

########################################### area dos metodos ##################################

def menu (a):   
    if a == 0:  #Aqui tem as condições
        sair () #Aqui chama outra função caso a condição seja satisfeita
    if a == 1:
        cadastrar()
    if a == 2:
        listar()

# Aqui se encontra as funções que serão chamadas na função menu

def sair ():
    print('Usuário(a) realizou Logoff')
def cadastrar():
    print('Cadastro de usuários')
def listar ():
    print('Lista de usuários cadastrados')

####################################### area do programa ###################################

#Aqui se encontra o cabeçalho 

print('==---'*20)
print('\nSelecione uma das opções válidas\n(0)SAIR\n(1)CADASTRAR\n(2)LISTAR\n')
print('==---'*20)
a = int(input('Sua opção:'))
menu(a)