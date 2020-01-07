#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matemática com Python
Um Guia Prático

Soluçao de Equações - Polinomiais 4

Exemplo 5.4

Autor: Guilherme A. Barucke Marcondes
"""
# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
from sympy import Symbol, solve


# Define uma nova função.
def calcula_f(x):
    return 3 * x**3 - 11 * x**2 + 5 * x + 3


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação 3*x**3 - 11*x**2 + 5*x + 3 = 0.')
print ('x =', resultado)
