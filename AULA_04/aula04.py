#ATIVIDADE PROPOSTA PELO PROF

#FAÇA UM PROGRAMA QUE LEIA DOIS NUMEROS
#REALIZE AS QUATRO OPERAÇÕES MATEMÁTICAS
#IMPRIMA NA TELA O RESULTADO
#INFORME QUAL É O MAIOR NÚMERO DIGITADO

num1 = int(input('Digite n1: '))
num2 = int(input('Digite n2: '))

soma = num1 + num2
sub = num1 - num2
div = num1 / num2
produto = num1 * num2

print('A soma de num 1 e num 2 é: {}\nA diferença de num 1 e num 2 é: {}\nA divisão de num1 e num 2 é: {}\nO produto de num1 e num 2 é: {}'.format(soma,sub,div,produto))

if num1 > num2:
    print('Num 1 é maior')
else:
    print('Num2 é maior')