# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python




# ----------------------------------------  DEFINIÇÃO DAS LISTAS E VARIÁVEIS  --------------------------------------------------
    #-- LISTAS
tripulantes = [] 
trip_aviao = []

    # -- STRINGS E CARACTERES
mov_ida = 'MOVIMENTAÇÃO FORTWO ( TERMINAL --> AVIÃO )'
mov_volta = 'MOVIMENTAÇÃO FORTWO ( AVIÃO --> TERMINAL )'
terminal = 'Tripulantes no Terminal --> '
aviao = 'Tripulantes no Avião --> '
multiplicador = '=-=-=-=-'
viagem = 0 #-- CONTADOR

# ------------------------------------------   DEFINIÇÃO DOS MÉTODOS   ---------------------------------------------------

    # -- MÉTODO QUE REALIZA A LEITURA DO ARQUIVO (TERMINAL.TXT) - PASSA OS DADOS DO ARQUIVOS PARA A LISTA (TRIPULANTES)
    
def ler():
    arq = open('C:\\Users\\900139\\Desktop\\GIT\\PYTHON_COURSE\\AULA_28\\terminal.txt','r')
    
    for pessoa in arq:
        pessoa = pessoa.strip()
        tripulantes.append(pessoa)
        
    arq.close
    return tripulantes

    # -- MÉTODO QUE REALIZA A ESCRITA DOS DADOS NA LISTA (TRIP_AVIAO) NO ARQUIVO (EMBARCADOS.TXT)
    
def add_embarcados():
    arquivo = open('C:\\Users\\900139\\Desktop\\GIT\\PYTHON_COURSE\\AULA_28\\embarcados.txt','w')
    for pessoas in trip_aviao:
        arquivo.write(f'{pessoas}\n')
    arquivo.close()

# ---------------------------------------  DESENVOLVIMENTO DO CÓDIGO  -----------------------------------------------

    # -- MÉTODO QUE CONTÉM A LÓGICA DO PROBLEMA E A RESOLUÇÃO 
    
def viagem_fortwo():

    if len(tripulantes) == 3:
        tripulantes[0], tripulantes[1] = tripulantes[1], tripulantes[0]


    global viagem
    viagem += 1
    print(f'{multiplicador * 6} VIAGEM {viagem} {multiplicador *6}')
    print(f'Embarque {viagem} (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
    print(mov_ida)
    print(f'{terminal} {tripulantes[2:]}')
    input('...')
    
    
    if len(tripulantes) == 2:
        trip_aviao.append(tripulantes.pop(0))
        trip_aviao.append(tripulantes.pop(0))
        
        print(trip_aviao)
              
    if len(tripulantes) == 6:
        trip_aviao.append(tripulantes.pop(0))
    
    if tripulantes:
        trip_aviao.append(tripulantes.pop(1))
        print(f'{aviao} {trip_aviao}')
        print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')
    else:
        print(f'{aviao} {trip_aviao}')
       
    input('...')
    
# ------------------------------------------------------------------------------------------------------------------------------

   # -- CHAMADA DOS MÉTODOS
   
ler()
    
for i in range(0,6): # -- LAÇO QUE FAZ A CHAMADA DO MÉTODO 6 VEZES (6 VIAGENS)
    viagem_fortwo()

add_embarcados()


# -----------------------------------  ESBOÇO DO PRIMEIRO CÓDIGO  --------------------------------------------------

#--------------- VIAGEM 01 ---------------
# print(f'{multiplicador * 6} {viagem} 01 {multiplicador *6}')
# print(f'Embarque 01 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(1))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 02 {multiplicador *6}')
# print(f'\n\nEmbarque 02 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(1))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 03 {multiplicador *6}')
# print(f'\n\nEmbarque 03 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(0))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 04 {multiplicador *6}')
# print(f'\n\nEmbarque 04 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(1))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 05 {multiplicador *6}')
# print(f'\n\nEmbarque 05 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(1))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 06 {multiplicador *6}')
# print(f'\n\nEmbarque 06 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(0))
# print(f'{aviao} {trip_aviao}')
# print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

# input('...')

# print(f'{multiplicador * 6} {viagem} 07 {multiplicador *6}')
# print(f'\n\nEmbarque 07 (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
# print(mov_ida)
# print(f'{terminal} {tripulantes[2:]}')
# input('...')
# trip_aviao.append(tripulantes.pop(0))
# trip_aviao.append(tripulantes.pop(0))
# print(f'{aviao} {trip_aviao}')


