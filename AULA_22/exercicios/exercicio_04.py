# Aula 21 - 09-12-2019
# Classe

# Na I Feira de Cerveja de Ituroró que irá acontecer em 2020, a AMBEV irá colocar 2 conteiners 
# de atendimento automatizado, um para bebidas alcoolicas e outro de bebidas não alcoolicas.
# O sistema irá operar da seguinte forma: 
# - O cliente se cadastrará no caixa retirando um cartão com um qrcod.
# - O cliente poderá recarregar o cartão com um determinado valor em dinheiro.
# - Quando o cliente chega no conteiner, passará o cartão em um leitor de qrcode que irá liberar 
# uma torneira da bebida de sua preferência. 
# -  Cada bebida tem um valor por ml que conforme enche o copo, irá descontando em tempo real, do 
# cartão do cliente.
# - Se o acabar os créditos, a torneira fecha autométicamente
# - Para a bebida alcoolica, só poderá ser liberada caso o cliente tenha mais de 18 anos.


# 1) Crie uma classe cliente que possui como atributos: Nome, idade, telefone.
# A variável nome e telefone deve ser um string. A variável idade deve ser valor inteiro.
# O cliente deve ter R$ 100.00 de dinheiro como saldo no cartão.
# 2) Crie metodos para: adicionar saldo no cartão, descontar saldo do cartão e verificar saldo do cartão.
# 3) para descontar o saldo do cartão, deve-se entra com a quantidade de ml e o valor por ml da bebida.
# O metodo deve imprimir na tela a quantidade de bebida e o valor descontado. Caso o saldo do cliente não
# seja o suficiente, deve-se imprimir o valor descontado e o volume liberado de bebida.


# Bebidas: 
# Refrigerante R$ 0,01 /ml 
# Cerveja ipa  R$ 0,05 /ml 
# Cerveja ale  R$ 0,063 /ml 