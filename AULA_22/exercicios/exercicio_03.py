# Aula 21 - 09-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreviativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Exceções como é!



class Cadastro:

    def __init__(self):
        self.lista = []
        # self.ler()
        pass


    def ler(self):
        try:
            arquivo = open('C:\Data\GitHub\PythonActivities\AULA_22\exercicios\cadastro2.txt', 'r')
            

            for pessoa in arquivo:

                pessoa = pessoa.strip().split(';') #  --> 6;Waldir;34;f;nandah.s2@bol.com.br;058903756441  <--
               
                dicio = {}

                dicio['cod'] = pessoa[0]
                dicio['nome'] = pessoa[1]
                dicio['idade'] = pessoa[2]
                dicio['sexo'] = pessoa[3]
                dicio['email'] = pessoa[4]
                dicio['tel'] = pessoa[5]
            
            self.lista.append(dicio)
        
        finally:
            arquivo.close()


    def salvar (self):
        try:
            arquivo = open('C:\Data\GitHub\PythonActivities\AULA_22\exercicios\cadastro2.txt', 'a')
            for pessoa in self.lista:
                texto = f"{pessoa['cod']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['tel']}"
                arquivo.write(texto)
        finally:
            arquivo.close()

    def cadastrar (self):
        nome = input('Digite o nome do cliente: ')
        idade = int(input('Digite a idade do cliente: '))
        sexo = input('Digite o sexo: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')

        codigo = str (int(self.lista[-1]['cod']) +1 )

        dic = {'cod': codigo, 'nome': nome, 'idade': idade, 'sexo': sexo, 'email': email, 'tel': telefone}
        self.lista.append(dic) 

    def consulta (self,codigo):

        for pessoa in self.lista:
            if int(pessoa['cod']) == codigo:
                print(f'''
                Cod: {pessoa['cod']}
                Nome: {pessoa['nome']}
                Idade: {pessoa['idade']}
                Sexo: {pessoa['sexo']}
                Email: {pessoa['email']}
                Telefone: {pessoa['tel']}
                ''')
                break

    def atualizar (self,codigo):
        for pessoa in self.lista:
            if int(pessoa['cod']) == codigo:
                nome = input('Digite o nome do cliente: ')
                idade = int(input('Digite a idade do cliente: '))
                sexo = input('Digite o sexo: ')
                email = input('Digite o email: ')
                telefone = input('Digite o telefone: ')
                # ATUALIZA OS DADOS:
                pessoa['nome'] = nome
                pessoa['idade'] = idade
                pessoa['sexo'] = sexo
                pessoa['email'] = email
                pessoa['tel'] = telefone

a = Cadastro()

print(a.ler())