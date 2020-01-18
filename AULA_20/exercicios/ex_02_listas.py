# Aula 20 - 05-12-2019

# DICA: use o metodo round(valor,2) para arredondar os numeros para fazer
# a conta. Assim evita que o python use valores muito quebrados para as 
# contas.
# Exemplo:
# >>> round(2.7555,2)
# 2.76

# DICA2: Há 3 operadores matemáticos para a divisão: / // e o %
# / - é a divisão total entre os dois números. Pode resultar em numeros 
# reais.
# Exemplo: 5 / 3 = 1.6666666666666667
# // - é a divisão inteira. Ela vai resultar em números inteiros
# Exemplo: 5 // 3 = 1
# % - é o resto da divisão inteira. É o que sobra.
# Exemplo: 5 % 3 = 2



# 1 - Caixa eletrônico 
# Com estas listas de  dicionários:

nota = [{'Nota(s)':100.00},{'Nota(s)':50.00},{'Nota(s)':20.00},
        {'Nota(s)':10.00},{'Nota(s)':5.00},{'Nota(s)':2.00},]
            
            
moeda = [{'Moeda(s)':1.00},{'Moeda(s)':0.50},{'Moeda(s)':0.25},
         {'Moeda(s)':0.10},{'Moeda(s)':0.05},{'Moeda(s)':0.01}]

# Monte um metodo que leia um valor e imprima (f-string) a quantidade de 
# cada nota(s) e moeda(s) necessária(s) para devolver o troco ao cliente.

