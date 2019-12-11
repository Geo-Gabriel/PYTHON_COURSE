# BHASKARA ( ax² + bx + c)

import math

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b**2) - 4 * a * c 

if delta < 0:
    print('Esta equação não possui raízes reais')
if delta == 0:
    