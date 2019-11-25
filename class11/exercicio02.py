# 2 - Crie um programa que calcule
#       a rentabilidade anual de um investimento
#       baseando-se em sua rentabilidade mensal ( juros composto )
#       a rentabilidade deve ser apresentada em % e em R$
#       utilizar métodos

# 
a = float(input('Digite o valor em R$: '))
b = float(input('Digite o valor do juros ao mes em porcentagem: '))
c = int(input('Digite quantos meses deseja investir: '))
print()

def juros_composto(a,b,c):
    calc = (a * (1 + b)**c)
    return calc

calc = juros_composto(a,b,c)

def rentabilidade(a,b):
    renta_r = a - b
    return renta_r

renta_r = rentabilidade(calc,a)


def renta_porcentagem (a):
    return (a / 100)

renta_porcen = renta_porcentagem(renta_r)

# print('calculo: {:.2f}, {:.2f}, {:.2f} % '.format(calc, renta_r, renta_porcen))

print("Seu investimento inicial foi {} R$\nCom aplicação de {} % A.M durante {} meses\n".format(a,b,c))
print()
print("O rendimento total ao longo desses {} meses foi de {:.2f}\nA rentabilidade em R$ foi de {:.2f} R$ que corresponde a {:.2f} %".format(c,calc,renta_r,renta_porcen))