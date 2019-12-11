#--- Exercício 4 - Funções - 2
#--- Crie uma função que realize o cálculo de contribuição do funcionário para a previdência da empresa
#--- O cálculo deve ser feito de acordo com a faixa salarial:
#---    De R$ 0000.00 Até R$ 1000.00 -> 1.0%
#---    De R$ 1000.01 Até R$ 3000.00 -> 1.5%
#---    De R$ 3000.01 Até R$ 6000.00 -> 2.0%
#---    Acima de R$ 6000.01 -> 2.5%
#--- A função deve receber o valor do salário
#--- A função deve fazer o cálculo de acordo com as regras de faixa salárial e atribuir o resultado em uma variável
#--- O resultado deve ser impresso pela função juntamente com uma frase e utilizando f-string
#--- Deve ser realizada a leitura do salário fora da função e armazenada em uma variável
#--- Chamar a função e passar a variável do salário criada durante a leitura do console


def calc_prev (a):
    if a <= 1000:
        a = (a * 0.01)
    elif a >= 1000.01 and a <= 3000:
        a = (a * 0.015)
    elif a >= 3000.01 and a <= 6000:
        a = (a * 0.020)
    else:
        a = (a * 0.025)
    return a
salario = float(input('Digite salário em R$: '))


print(f'''Recolhimento é de {calc_prev(salario) :.2f} R$ tendo como base a tabela abaixo:\n 
R$ 0000.00 Até R$ 1000.00 -> 1.0%
De R$ 1000.01 Até R$ 3000.00 -> 1.5%
De R$ 3000.01 Até R$ 6000.00 -> 2.0%Acima de R$ 6000.01 -> 2.5%''')

calc_prev(salario)