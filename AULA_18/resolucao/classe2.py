
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
        dfgdfshkgjhsdkjhgkjsdhghjksd
        '''
        arquivo = open('18-Aula18/exercicios/cadastro.txt','r')
        self.lista = []
        for pessoas in arquivo:
            pessoas = pessoas.strip().split(';')
            dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 
                            'sexo':pessoas[2], 'idade':pessoas[3]}
            self.lista.append(dicionario)
        arquivo.close()
        return self.lista

    def lista_festa(self):
        '''
        lkjgfsddfsglgdfsljdgfllkjljk
        '''
        lista_homens = []
        lista_mulheres = []

        for pessoa in self.lista:
            if int(pessoa['idade']) >= 18:
                if pessoa['sexo'] == 'f':
                    lista_mulheres.append(pessoa)
                else:
                    lista_homens.append(pessoa)

        self.salvar(lista_homens,'homens')
        self.salvar(lista_mulheres,"mulheres")
        
    def salvar(self,lista1,nome):
        '''
        gllljklkj jhouioiuoi klkkllk
        '''
        arquivo = open(f'18-Aula18/exercicios/{nome}.txt','a')
        for pessoa in lista1:
            texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
            arquivo.write(texto)
        arquivo.close()

    def consulta(self,numero):
        '''
        gggggggggggggggggggggggggg
        '''
        for lista_consulta in self.lista:
            if int(lista_consulta['codigo']) == numero:

                if int(lista_consulta['idade']) >= 18:
                    if lista_consulta['sexo'] == 'f':
                        print(f"Nome: {lista_consulta['nome']} valor ingresso: R$ 15,00 ")
                    else:
                        print(f"Nome: {lista_consulta['nome']} valor ingresso: R$ 35,00 ")
                else:
                    print(' Não Pode Entrar!')






