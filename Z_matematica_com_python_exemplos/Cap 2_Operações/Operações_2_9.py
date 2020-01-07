#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matemática com Python
Um Guia Prático

Operações - Frações

Exemplo 2.9

autor: Guilherme A. Barucke Marcondes
"""
# Importa função Fraction (fração) da biblioteca fractions.
from fractions import Fraction

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define frações.
a = Fraction(1, 4)  # a = 1/4
b = Fraction(2, 3)  # b = 2/3

# Operações.
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print (u'Resultado das operações com frações.')
print ('a =', a)
print ('b =', b)
print ('a + b =', soma)
print ('a - b =', subtracao)
print ('a * b =', multiplicacao)
print ('a / b =', divisao)
