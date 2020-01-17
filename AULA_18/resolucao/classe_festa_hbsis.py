class FestaHBSIS:
    '''
    A classe da festa HBSIS é uma classe que controla a entrada da festa restrita
    de arromba que a HBSIS promove 1 vez a cada ano. Coincidentemente é quando o
    chefe sai com a familia para viajar até a  europa e só volta o ano que vem.
    Conhecida como a festa de vai e não volte peloamordedeus!
    '''
    def __init__(self):
        '''
        i __init__ é para iniciar as variáveis e disponibiliza-las para todos os 
        metodos da classe.
         O self é a ponta que irá conectar toda a classe e seus atributos
         atributos são variáveis!
        '''
        self.lista = self.ler_cadastro()

    def ler_cadastro(self):
        '''
        Este metodo lê o arquivo e converte os dados em uma biblioteca retornando 
        para a classe e depois o código fonte.
        '''
        arquivo = open('18-Aula18/exercicios/cadastro.txt','r')
        self.lista = []
        for dados in arquivo:
            dados = dados.strip()
            dados = dados.split(';')
            pessoas = {'codigo':dados[0],'nome':dados[1], 'sexo':dados[2], 'idade':dados[3]}
            self.lista.append(pessoas)
        arquivo.close()
        return self.lista

    def __salvar(self,lista_salvar,nome_arquivo):
        '''
        Este metodo salva os dados da lista passada em um arquivo.
        '''
        arquivo = open(f'18-Aula18/exercicios/{nome_arquivo}.txt','a')
        for pessoa in lista_salvar:
            linha = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
            arquivo.write(linha)
        arquivo.close()

    def lista_festa(self):
        '''
        este metodo pega a lista e separa us menor dos adultos e envia para salvar a fim de
        gravar a lista nos arquivos desejados.
        '''
        lista_feminina = []
        lista_masculina = []
        for pessoas in self.lista:
            if int(pessoas['idade'])>=18: 
                if pessoas['sexo']=='f':
                    lista_feminina.append(pessoas)
                else:
                    lista_masculina.append(pessoas)
        self.__salvar(lista_feminina,'mulheres')
        self.__salvar(lista_masculina,'homens')
        

    def entrada(self,codigo_cadastro):
        '''
        Este metodo verifica se a pessoa pode ir para a festa e qual o preço do ingresso
        '''
        for pessoas in self.lista:
            if int(pessoas['codigo']) == codigo_cadastro:
                if int(pessoas['idade']) >= 18: 
                    if pessoas['sexo']=='f':
                        print(f"Nome: {pessoas['nome']} ingresso: R$ 15,00")
                    else:
                        print(f"Nome: {pessoas['nome']} ingresso: R$ 35,00")
                else:
                    print('Entrada Proibida!')
        