# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante

lista = []
def five ():
    while True:
        j = 1
        try:
            for i in range(5):
                n = int(input(f'Digite número ({j}): '))
                j += 1
                lista.append(n)
        except ValueError:
            print('Digite um número válido')
        else:
            break

        finally:
            print(lista)
            print('FIM')
            break
            
lista_five = five()

lista_ret = []

for n in five():
    a = n * 5
    print(a)
    lista_ret.append(a)
