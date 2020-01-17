# 1 - o programa deve ter um menu interativo com cabeçalho, local para: Cadastro de clientes,
# ver clientes cadastrados, cadastro de produtos, ver produtos cadastrados, venda de produtos,
# relatório de vendas e a opção sair. 
# Este meni deve se reptir até que a opção sair for chamada. 

                # Aqui o menu fica salvo em uma variável podendo solicitar a qualquer momento
menu = ''' 
#############################################################################################################
#                                      I Festival de cerveja de Ituroró                                     #
#############################################################################################################

1:..>> Cadastro de Clientes
2:..>> Ver Clientes Cadastrados
3:..>> Cadastro de produtos
4:..>> Ver Produtos Cadastrados
5:..>> Vendas de Produtos
6:..>> Relatório de Vendas
7:..>> Sair 

Digite a opção desejada >>  '''

#opcao = input(menu) # O laço de repetição torna o menu interativo. 
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Clientes')
    elif opcao == '2':
        print('Ver Clientes Cadastrados')
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Ver Produtos Cadastrados')
    elif opcao == '5':
        print('Vendas de Produtos')
    elif opcao == '6':
        print('Relatório de Vendas')
    elif opcao == '7':
        print('Sair')
        break # A
    else:
        print('Valor inválido')
    