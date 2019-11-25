# AULA 11 --- 21-11-2019
# PROVAAA 

# 1- Crie um programa que calcule 
#       o imposto ISS de um serviço de desenvolvimento de software - Utilizar métodos


def imposto(a):
    return a * 0.0025

servico = imposto(float(input('Digite o valor do serviço de desenvolvimento de software: ')))

print('Imposto: {:.2f}'.format(servico))