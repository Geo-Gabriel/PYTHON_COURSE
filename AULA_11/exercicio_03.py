# 2 - Crie um programa para calculo de investimento
#       solicitar valor a ser investido na tesouro SELIC
#       considerar o valor SELIC de hoje
#       calcular o valor total ate o vencimento do titulo
#       utilizar métodos


valor_investido = float(input('Digite o valor a investir: '))

selic = 10410

cotas = float(input('quantas cotas: '))

valor_cota = cotas * selic

print(valor_cota)

parte_selic = selic / 100
taxa_selic = parte_selic + 0.0002
