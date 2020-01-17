# Aula  17 --- 02-12-2019
# Dicionários, While

bole = True
n = 0 

while False:
    n = n + 1
    print(f'Hello mundo - {n}')

while n <= 30:
    n = n + 1
    print(f'Hello mundo - {n}')
    break
    print('Passou!!')

while n <= 30:
    n = n + 1
    print(f'Hello mundo - {n}')
    if n == 10:
        continue
    print('Passou!!')