# PROGRAMA DE BOAS VINDAS
print('='*30)
print('Questionário sobre o crime')
print('='*30)
print()
print('Digite 01 para afirmativa ou 0 para negativa')
print()
p1 = int(input('Telefonou para a vítima?: ')) 
p2 = int(input('Esteve no local do crime?: ')) 
p3 = int(input('Telefonou para a vítima?: ')) 
p4 = int(input('Mora perto da vítima?: ')) 
p5 = int(input('Já trabalhou com a vítima?: ')) 

soma = (p1+p2+p3+p4+p5)

if soma == 2:
    print('Classificado como suspeito')
if 3 <= soma <= 4:
    print('Classificado como cumplice')
if soma == 5:
    print('Assasino da vitima')
if soma == 0:
    print('Classificado como Inocente')