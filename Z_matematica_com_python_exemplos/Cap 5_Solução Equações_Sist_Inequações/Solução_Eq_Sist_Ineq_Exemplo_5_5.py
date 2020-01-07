#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matemática com Python
Um Guia Prático

Solução de Equações - Trigonométricas 1

Exemplo 5.5

Autor: Guilherme A. Barucke Marcondes
"""

# Importa Symbol - possibilidade de operações com símbolos.
# Importa solve - permite solução de equações.
# Importa função seno (sin).
from sympy import Symbol, solve, sin


# Define uma nova função.
def calcula_f(x):
    return sin(4 * x) - 1


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define x como uma variável.
x = Symbol('x')

# Resolve a equação calcula_f = 0.
y = calcula_f(x)

resultado = solve(y)

print (u'\n Resultado da equação sin(4*x) - 1 = 0.')
print ('x =', resultado)
