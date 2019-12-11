#--- Exercicio 4  - Variávies e impressão com interpolacão de string
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()

a = '='
b = '°'
c = '\n'
viagem = '\tJaraguá do Sul/SC até Acre/AC via Terresre'
parada_1 = 'Jaraguá do Sul - 14/12/2020 - 12:26'
parada_2 = 'Joinville - 14/12/2020 - 13:30'
parada_3 = 'Curitiba - 14/12/2020 - 17:50'
parada_4 = 'Santos - 14/12/2020 - 23:10'
parada_5 = 'São Paulo - 15/12/2020 - 02:26'
parada_6 = 'Campinas - 15/12/2020 - 05:55'
parada_7 = 'Araraquara - 15/12/2020 - 11:58'
parada_8 = 'Uberaba - 15/12/2020 - 15:44'
parada_9 = 'Belo Horizonte - 15/12/2020 - 20:28'
parada_10 = 'Acre - 19/12/2020 - 00:00'


print(f'{a *60} \n{viagem} \n{a*60}')

print(' {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} '.format(b,parada_1,c,b,parada_2,c,b,parada_3,c,b,parada_4,c,b,parada_5,c,b,parada_6,c,b,parada_7,c,b,parada_8,c,b,parada_9,c,b,parada_10,c,))