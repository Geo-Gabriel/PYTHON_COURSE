# Crie um prorama que:
# 1 - leia dois numeros inteiros
# 2 - Calcule a soma entre is dois numeros atraves de um metodo
# 3 - Calcule a subtração entre is dois numeros atraves de um metodo
# 4 - Calcule a multiplicação entre is dois numeros atraves de um metodo
# 5 - Calcule a divisão entre is dois numeros atraves de um metodo
# 6 - Calcule a divisao fracionada entre is dois numeros atraves de um metodo
# 7 - Calcule a resto da divisao is dois numeros atraves de um metodo
# 8 - Calcule a raiz entre is dois numeros atraves de um metodo
# 9 - Separa os metodos em outros arquivos

from metodos_operacoes import soma, subtracao, divisao, divisao_fracionada, resto_divisao, raiz_a_b

a = int(input('Digite a:'))
b = int(input('Digite b: '))

print(f'Soma: {soma(a,b)}\nSubtração: {subtracao(a,b)}\nDivisao: {divisao(a,b)}')


#print(f'Soma: {resul_soma}\nSubtração: {resul_sub}\nProduto: {resul_produto}\nDivisão Inteira: {resul_divisao_inteira}\nDivisao Fracionada: {resul_divisao_fracionada}\nResto Divisao: {resul_resto_divisao}\nRaiz dos numeros: {resul_raiz}')

# -------------------------------------------- Métodos --------------------------------------

# def soma (a,b):
#     soma_n = a + b
#     return soma_n

# resul_soma = soma(a,b)


# def subtracao (a,b):
#     subtracao_n = a - b
#     return subtracao_n

# resul_sub = subtracao(a,b)


# def produto (a,b):
#     produto_n = a * b
#     return produto_n

# resul_produto = produto(a,b)


# def divisao (a,b):
#     divisao_n = a // b
#     return divisao_n

# resul_divisao_inteira = divisao(a,b)


# def divisao_fracionada (a,b):
#     divisao_fracionada_n = a / b
#     return divisao_fracionada_n

# resul_divisao_fracionada = divisao_fracionada(a,b)


# def resto_divisao (a,b):
#     resto_divisao_n = a % b
#     return resto_divisao_n

# resul_resto_divisao = resto_divisao(a,b)


# def raiz_a_b (a,b):
#     base_raiz = a 
#     indice_raiz = a ** (1/b)
#     return indice_raiz

# resul_raiz = raiz_a_b(a,b)
