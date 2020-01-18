# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# Não há nada mais chato na programação quando um erro acontece.
# O Python tem como filosofia não deixar o erro passar em branco.
# Porem há erros que podem ocorrer mas não por nossa 
# responsabilidade.

# Exemplos: 
# - Alguem apagou o arquivo que seria de leitura.
# - Caiu a rede na hora de comunicar e salvar dados no banco de
# dados.
# - Alguem por acidente executou o script sql errado e apagou o 
# banco de dados.
# - Em Web Scraping, um dos sites que vocês querem coletar dados
# saiu fora do ar.
# - No campo: "Digite quantos filhos você tem?" a pessoa escreveu:
# "Tenho uma menina e um menino" quando deveria digitar somente o
# número 2!

# ATENÇÃO! Silenciar o erro não deve ser uma pratica para incubrir
# código ruin! 

# Por que silenciar o código?
# Todo erro do python causa interrupção imediata do código e
# esta interrupção encerra o programa. Ao silenciar o erro, o 
# programa passa a tratar este erro de forma diferente conforme 
# o programador queira.


# Quando usar?
# Quando uma parte do código funciona, mas em determinada condição
# ele pode aparecer um erro. Exemplo: Digitar uma string ao inves
# de um valor inteiro.

# Quando um erro pode finalizar um processo, porem o arquivo ou
# conecção não foi fechada. ( arquivo.close() )

# Quais erros existem?
# Pode ser encontrado os erros e seus significados no site:
# https://docs.python.org/3.7/library/exceptions.html

# Aqui em baixo está a arvore de erros do Python 3.7: 

#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError 
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


# Quais as formas de executar a excessão?
# 

try:
    #digitar um código
except:
    # O que fazer se um erro aparecer.

# Neste caso, o except não possui uma indicação do erro.
# ISSO NÂO É INDICADO FAZER! 
# > KeyboardInterrupt (interrupção pelo teclado. quando digita Ctrl+c 
# na execução do código)
# > MemoryError (Quando não há mais memória livre
# podendo causar a perda de informação ou má execução do código)


# A forma mais correta é indicar o erro. Assim se surgir outro erro, pode-se analizar


try:
    # Código fonte
except NomeErro:
    # Código que executa quando o erro "NomeErro" é acionado.
    # Pode-se adicionar uma tupla contendo vários erros.
    # Ou pode ter vários except com vários erros e o tratamento para cada um deles.
else:
    # Se não houver erro, este será executado. Este não será executado 
    # quando o break for acionado no try.
finally:
    # Este código sempre será executado, independente se há erro ou não.
    # É uma forma de fechar coneção ou arquivo (.close()) autométicamente.



try:
    inteiro = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro}')
    inteiro2 = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro2}')
    print(f'{inteiro}/{inteiro2} = {inteiro/inteiro2}')
    break
except ValueError:
    print('Você digitou o número errado - ValueError')
except NameError:
    print('#### há algo errado #### - NameError')
except ZeroDivisionError:
    print('Você tentou dividir por ZERO! - ZeroDivisionError')
else:
    print('Codigo no ELSE')
finally:
    print('Fim!')


try:
    inteiro = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro}')
    inteiro2 = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro2}')
    print(f'{inteiro}/{inteiro2} = {inteiro/inteiro2}')
    #break
except (ValueError,NameError,ZeroDivisionError):
    print('#### há algo errado ####')
else:
    print('Codigo no ELSE')
finally:
    print('Fim!')

# Para saber um pouco mais no que você errou, pode-se usar o comando "as" e uma variável.
# assim pode-se trabalhar ou printar informações do erro sem prejudicar o andamento do 
# programa.


try:
    inteiro = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro}')
    inteiro2 = int(input('Digite um número: '))
    print(f'você digitou o número {inteiro2}')
    print(f'{inteiro}/{inteiro2} = {inteiro/inteiro2}')
    #break
    
except (ValueError,NameError,ZeroDivisionError) as erro1:
    salvar_erro = erro1
    print('#### há algo errado ####\n\n',erro1,'\n\n')
    print('#### há algo errado ####\n\n',salvar_erro,'\n\n')
else:
    print('Codigo no ELSE')
    ficar = False
finally:
    print('Fim!')

# Aqui foi usado a variável erro1 para poder capturar este erro e ser printado
# logo a baixo. Porem o erro1 é destruido quando o try é finalizado.

    

try:
    arquivo = open('lista.txt','r')
except OSError:
    print('Houve um erro! Arquivo não foi aberto')
else:
    print('Tudo certo! Arquivo aberto!')
finally:
    if 'arquivo' in dir():
	    print('fechando arquivo se ele existir')
	    arquivo.close()



# Dica!
# if 'arquivo' in dir(): Verifica se a variável exite neste escopo

# class Pessoa:
#   def __init__(self):
#        self.a = 0
# armando = Pessoa()
# if 'a' in dir(armando): verifica se exite uma variável na classe Pessoa.

# if 'variavel' in locals(): Verifica se há uma variavel local

# if 'variavel' in globals(): Verifica se há uma variavel global


# O comando raise força um erro determinado e mostra uma mensagem personalizada de
# erro.

try:
    raise NomeErro('Mensagem de Erro!')
except NomeErro:
    print('Esta é uma exceção NomeErro')
    raise

# O NomeErro deve ser um erro que esteja na arvore de erro mencionado acima exemplo 
# ValueError

# O raise no final acaba chamando o erro que foi evitado assima. Assim pode-se verificar 
# se o erro está funcionando.


# O assert irá retornar um erro caso o teste condicional for FALSO! 
# O erro retornado será o AssertionError
assert nun == 2, 'Conta está errada'




try:
    inteiro = int(input('Digite o valor a ser dividido: '))
    inteiro2 = int(input('Digite o valor do divisor: '))
    assert not inteiro2 == 0, 'Divizor não pode ser zero!'
except AssertionError:
    print('#### Cabeção! Digitou errado! O divizor não pode ser zero! ###','\n'*3)
    raise











































































































# DICA oculta:
# O "import os" pode habiliar alguns comandos como o os.system() que pode passar comando 
# do DOS, shell script do python para o terminal.
# 
# Como vocês ainda não sabem o que é o import e como ele funciona, então o pode-se trocar por:
# 
# from os import system
# system('dir')
#
# Agora imagine se usar o system('cls') para windows ou system('clear') para linux
# :-)
# Poste no grupo do whatsapp #ACHEI! se vc ler esta mensagem!