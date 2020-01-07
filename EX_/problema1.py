#A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: 
# a tripulação técnica e a tripulação de cabine
# A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. 
# Por política da empresa, apenas o piloto e o chefe de serviço de voo podem dirigir este veículo. 
# É também política da empresa que nenhum dos oficiais pode ficar sozinho com o chefe de serviço de bordo
# e nem nenhuma das comissárias pode ficar sozinha com o piloto.
# No terminal de embarque estão os seis tripulantes e ainda um policial junto com um presidiário.
# Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

#dois grupos : 
#               Tripulacao_Tecnica:
#                                    1-Piloto
#                                    2-Oficiais
#               Tripulacao_Cabine:
#                                   1-Chefe de servico
#                                   2-Comissarias

#Transporte entre terminal e o avião feito pelo SmartFortwo
#Leva apenas duas pessoas
#Apenas o Piloto e o Chefe de servico pode dirigir  - Policial tambem
#Comissarioas não podem ficar com o piloto
#Oficiais não podem ficar com o Chefe de servico
#Precidiario não pode ficar sem o policial

lista_terminal = ['Piloto','Oficial1', 'Oficial2', 'Chefe de Servico','Comissaria1','Comissaria2','Policial','Presidiario']
lista_aviao = []

def imprime_cabecalho():
    print('='*50)
    print('\rA HBSIS Airlines','\n'*2)

def imprime_rodape():
    print('\n'*2)
    print('='*50)

def imprime_terminal_aviao():
    print(f'Pessoas que estão no terminal: {lista_terminal} ')
    print(f'Pessoas que estão no aviao: {lista_aviao} ')

def embarcar_fortwo(motorista, passageiro):
    print('\nIniciando embarque no fortwo...')
    lista_terminal.remove(passageiro)
    print(f'Realizando a viagem com o Fortwo: motorista: {motorista} - passageiro: {passageiro}')
    embarcar_aviao(passageiro)    
    print(f'{motorista} - Voltanto para o terminal')
    print(f'Chegada no terminal! {motorista} volta ao terminal')

def embarcar_aviao(pessoa):
    print('Desenbarcando do Fortwo...')
    print(f'{pessoa} embarcando no aviao ...')
    lista_aviao.append(pessoa)

def realizar_viagem(motorista, passageiro):    
    embarcar_fortwo(motorista,passageiro)  
    imprime_terminal_aviao()



imprime_cabecalho()
imprime_terminal_aviao()

realizar_viagem(lista_terminal[6],lista_terminal[7])
realizar_viagem(lista_terminal[0],lista_terminal[6])
realizar_viagem(lista_terminal[0],lista_terminal[1])
realizar_viagem(lista_terminal[0],lista_terminal[1])
realizar_viagem(lista_terminal[1],lista_terminal[0])
realizar_viagem(lista_terminal[0],lista_terminal[1])
realizar_viagem(lista_terminal[0],lista_terminal[1])


imprime_rodape()