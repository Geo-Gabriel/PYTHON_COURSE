# Aula 21 - 12-12-2019
# Cadastro do produto.

# Crie uma classe para o cadastro do produto, ler e gravar em arquivo .txt,
# atualizar produtos, e pesquisa pelo código de produto. (use como base a classe 
# cadastrar cliente)

# Para guardar os produtos importe a classe do exercicio 3 e atribua numa lista.


class CadastroProduto:
    def __init__(self):
        pass

    def ler_arquivo(self,nome_arquivo):
        '''
        Este metodo serve para ler um arquivo .txt que deve possuir os 
        dados dos produtos cadastrados.
        Vai receber como parametro o nome do arquivo (nome_arquivo) a ser 
        lido.
        Os dados lidos devem ser atribuidos a classe produto.
        '''
        pass

    def cadastro_produto(self):
        '''
        Este metodo é utilizado para cadastrar um produto.
        Os dados devem ser aplicados em uma classe produto.
        O codigo produto não pode se repetir e deve estar na sequencia númerica
        Neste caso se faz necessário adicionar linha no arquivo de texto com o metodo
        gravar adicionando os novos produtos (use o atributo 'a')
        '''
        pass

    def pesquisa_codigo(self,codigo):
        '''
        Neste metodo é feito a pesquisa do produto, mostrando os 
        dados do mesmo.
        No caso perguntará se vai querer alterar os dados.
        Se sim, altere e encaminhe para o metodo gravar.
        Lembrando que no caso de alteração, será necessário fazer a gravação de
        todos os dados usando o atributo 'w'.
        '''
        pass

    def gravar(self,nome_arquivo,atributo):
        '''
        Este é responsável por gravar os dados.
        use o atributo 'w' para sobrescrever o arquivo e o
        atributo 'a' para adicionar linha.
        o parametro nome_arquivo é o nome do arquivo em que se deseja gravar.
        '''
        pass