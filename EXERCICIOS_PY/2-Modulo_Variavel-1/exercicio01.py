#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

nome_f = input('Digite primeiro nome do funcionário: ')
sobrenome_f = input('Digite sobrenome nome do funcionário:')
cpf_f = input('Digite CPF do com pontos e traços: ')
rg_f = input('Digite o RG do com pontos e traços: ')
salario_f = float(input('Digite o salário do funcionário: '))

print('Nome: {}\nSobrenome: {}\nCPF: {}\nRG: {}\nSalário: R$ {:.2f}'.format(nome_f,sobrenome_f,cpf_f,rg_f,salario_f))