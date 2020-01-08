# Importando as bibliotecas necessárias
import matplotlib.pyplot

nome = ['George','Gabriel','Marciano','Pedro','Joao','Guilherme','Macarraõ']

valores = [value**2 for value in range(1,7)]

matplotlib.pyplot.plot(nome, valores)

matplotlib.pyplot.show()