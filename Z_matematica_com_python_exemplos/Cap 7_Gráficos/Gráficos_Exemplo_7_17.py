#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matemática com Python
Um Guia Prático

Gráficos - Formatação

Exemplo 7.17

Autor: Guilherme A. Barucke Marcondes
"""

# Importa função de elaboração de gráficos da biblioteca pylab.
# Função plot para plotar o gráfico.
# Função arange para definir as faixas de valores.
# Função yscale para alterar escala do eixo vertical.
# Função xscale para alterar escala do eixo horizontal.
# Função title para incluir nome no gráfico.
# Funções figure e subplot para exibir mais de um gráfico.
from pylab import plot, arange, yscale, xscale, subplot, title, subplots_adjust

# Limpa a área de console para facilitar a visualização do resultado.
print ('\n' * 100)

# Define valores a serem plotados no gráfico.
x = arange(0, 4, 0.5)  # Faixa de valores para x.
y = 2 * x
y1 = 3 * y
y2 = y ** 2

# Ajusta espaçamento entre os gráficos.
subplots_adjust(
    left=0.125, bottom=0.1, right=0.9, top=1.1, wspace=0.2, hspace=0.4)

# Exibe gráfico com várias sequências de pontos.
# Gráfico com triângulos verdes, círculos vermelhos e traços azuis.

subplot(221)
plot(x, y, 'g^', x, y1, 'ro', x, y2, 'bs')
title('Grafico 1')

subplot(222)
yscale('log')  # Muda escala do eixo vertical para log.
plot(x, y, 'k*', x, y1, 'cd', x, y2, 'mp')
title('Grafico 2 - Eixo y Escala Log')

subplot(223)
plot(x, y / 2, 'yh', x, 2 * y1, 'wo', x, y2 / 3, 'gx')
title('Grafico 3')

subplot(224)
xscale('log')  # Muda escala do eixo horizontal para log.
plot(x ** 2, y, 'kv', x ** 3, y1, 'c8', x ** 2.5, y2 / 2, 'b.')
title('Grafico 4 - Eixo x Escala Log')
