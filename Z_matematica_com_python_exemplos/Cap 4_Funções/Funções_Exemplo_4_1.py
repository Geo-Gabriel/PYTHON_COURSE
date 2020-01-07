#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matemática com Python
Um Guia Prático

Funções - Definição 1

Exemplo 4.1

Autor: Guilherme A. Barucke Marcondes
"""


# Define uma nova função. Neste caso, de uma única variável independente x.
def calcula_f(x):
    return 2 * x


# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Chama a função para calcular o valor para x = 3.0.
x = 3.0
y = calcula_f(x)

print ('Resultado da função calcula_f(x) para x = 3.')
print ('y =', y)
