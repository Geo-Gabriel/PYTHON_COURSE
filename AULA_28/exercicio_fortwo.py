tripulantes = ['Piloto','Oficial 1','Oficial 2',' Chefe Serviço Voo','Comissária 1','Comissária 2'
,'Policial','Presidiário']

mov_ida = 'MOVIMENTAÇÃO FORTWO ( TERMINAL --> AVIÃO )'
mov_volta = 'MOVIMENTAÇÃO FORTWO ( AVIÃO --> TERMINAL )'
terminal = 'Tripulantes no Terminal --> '
aviao = 'Tripulantes no Avião --> '
trip_aviao = []
multiplicador = '=-=-=-=-'
viagem = 0

def viagem_fortwo():

    global viagem
    viagem += 1
    print(f'{multiplicador * 6} VIAGEM {viagem} {multiplicador *6}')
    print(f'Embarque {viagem} (in fortwo) -- {tripulantes[0]} e {tripulantes[1]}')
    print(mov_ida)
    print(f'{terminal} {tripulantes[2:]}')
    input('...')
    trip_aviao.append(tripulantes.pop(1))
    print(f'{aviao} {trip_aviao}')
    print(f'{mov_volta} -- in fortwo: {tripulantes[0]}')

    if len(tripulantes) == 6:
        trip_aviao.append(tripulantes.pop(0))

    input('...')

    if len(tripulantes) == 1:
        trip_aviao.append(tripulantes.pop(0))
        print(f'{aviao} {trip_aviao}')

for i in range(0,7):
    viagem_fortwo()

# #--------------- VIAGEM 01 ---------------
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


