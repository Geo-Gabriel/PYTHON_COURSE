## EXERCICIOS FOR -- EM DICIONARIOS -- LISTAS ---  TUPLAS

dias_do_mes = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

qual_mes = int(input('Digite o numero do Mês para saber os dias: '))

print(f'O mês {qual_mes} tem {dias_do_mes[qual_mes]} dias')

print('Dias que faltam para acabar o ano... ')


print(sum(list(dias_do_mes.values())[qual_mes -1:])) # Aqui esta trabalhando so com os valores (soma dos valores)

total = 0 # Aqui nao esta contando, isso é um acumulador que vai retornar um valor acumulado no final

for mes in range(qual_mes,12+1): # usa range pois sabemos que vai começar de um determinado ponto até outro
    total += dias_do_mes[mes]   ## Total = total + dias_do_mes[mes] ----- Acumulando
print('modo estruturado')
print('total de dias até final do ano' , total) # Aqui retorna o valor acumulado

for chaves in dias_do_mes:
    print('tem uma chave aqui',chaves)
    print('para cada chave tem um valor', dias_do_mes[chaves])

for chave, valor in dias_do_mes.items():        # Aqui me retorna a chave e o valor (items)
    print('para a chave', chave, 'o valor é', valor)


################################# FOR EM TUPLAS ###############################

tupla = (1,1.5,'hello',int,str)

for itens in tupla:
    print (tupla)