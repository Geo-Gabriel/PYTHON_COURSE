#--- Exercicio 2  - Variávies e impressão com interpolacão de string
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format() para concatenar os números da opções, que devem ser números inteiros
#--- Alem das opções o menu deve conter um cabeçalho e um rodapé
#--- O cabeçalho e o rodapé devem ser impressos utilizando a multiplicação de caracters
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

print('=-='*40)
print('                                          CADASTRO DE FUNCIONÁRIOS V.1.0')
print('=-='*40)
print('\n\n\n')

print('01- Nome do funcionário     02- CPF      03- RG      04- Endereço        05- Idade       06- Estado Civil\n\n')


opc = int(input('Digite a opção desejada: \n'))

while opc != 0:

    if opc == 1:
        nome_f = input('Digite nome do funcionário: ')
    elif opc == 2:
        cpf_f = input('Digite CPF do funcionário: ')
    elif opc == 3:
        rg_f = input('Digite RG do funcionário: ')
    elif opc == 4: 
        ende_f = input('digite endereço do funcionário:')
    elif opc == 5:
        idade_f = int(input('Digite idade do funcionário: '))
    elif opc == 6:
        est_civil_f = input('Digite estado civil do funcionário: ')

    opc = int(input('Digite a opção desejada: \n'))