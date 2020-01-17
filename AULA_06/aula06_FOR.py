# TRABALHADO COM LAÇO DE REPETIÇÃO FOR 


# FOR SIMPLES USANDO RANGE NO INTERVALO DE 0 A 10 COM INCREMENTO DE UM
for i in range (0,10):
    print(f'{i} - LOVE U')

# FOR SIMPLES UTILIZANDO RANGE NO INTERVALO DE 0 A 10 COM INCREMENTO DE 2

for a in range (0,10,2):
    print(f'{a} - TESTE')


# O MELHOR A SE UTILIAR EM UMA LISTA NÁO É O FOR COMO RANGE E SIM O FOR IT 
# USA O FOR COMO RANGE QUANDO QUER IMPRIMIR UMA QUANTIDADE ESPECIFICA DE VEZES

lista = ['george', 'gabriel', 'pereira', 'da']

for nomes in lista:
    print(nomes)

lista.append('silva')

n = int(input('Digite n:'))

for i in range (0,11):
    print(f'{i} x {n} = {i*n}')