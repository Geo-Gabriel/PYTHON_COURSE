#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

a = ''
b = ''
c = ''

def media (a,b,c):
    a = float(input('Digite a: '))
    b = float(input('Digite b: '))
    c = float(input('Digite c: '))
    media = (a + b + c) / 3
    return media

media = media(a,b,c)

print(f'A média de a + b + c é {media :.2f}')