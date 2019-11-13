
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a primeira nota do aluno: '))
n3 = float(input('Digite a primeira nota do aluno: '))
n4 = float(input('Digite a primeira nota do aluno: '))

# MÉDIA ARITMÉTICA DAS NOTAS

media = (n1 + n2 + n3 + n4 ) / 4

######################################################

if n1 == n2 and n2 == n1:
    print('n1 e n2 iguais: {} e {}'.format(n1, n2))

if n1 == n3 and n3 == n1:
    print('n1 e n3 iguais: {} e {}'.format(n1,n3))

if n1 == n4 and n4 == n1:
    print('n1 e n4 iguais: {} e {}'.format(n1, n4))

if n2 == n3 and n3 == n2:
    print('n2 e n3 iguais: {} e {}'.format(n2,n3))

if n2 == n4 and n4 == n2:
    print('n2 e n4 iguais: {} e {}'.format(n2,n4))

if n3 == n4 and n4 == n3:
    print('n3 e n4 iguais: {} e {}'.format(n3, n4))

# VERIFICA QUAL É A MAIOR NOTA E IMPRIME NA TELA
# UTILIZANDO OPERADORES RELACIONAIS E LÓGICOS

lista = [n1, n2, n3, n4]
print('maior nota: ', max(lista))

#######################################################

# VERIFICA QUAL É A MENOR NOTA E IMPRIME NA TELA
# UTILIZANDO OPERADORES RELACIONAIS E LÓGICOS

lista = [n1, n2, n3, n4]

print('menor nota: ', min(lista))
#######################################################


# IMPRIME A MÉDIA DAS NOTAS E IMPRIME SE FOI APROVADO OU REPROVADO COM BASE 
# NA NOTA DE CORTE QUE É 7.0

if media >= 7:
    print('Aprovado com média de: ', media)
else:
    print('reprovado com média de: ', media)
