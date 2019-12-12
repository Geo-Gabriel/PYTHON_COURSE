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

        pass


    def print(self):
        arquivo = open('C:\Data\GitHub\PythonActivities\AULA_22\exercicios\cadastro2.txt', 'r')
        lista = []
        for linhas in arquivo:

            linhas = linhas.strip().split(';')
            dicio = {}

            dicio['cod'] = linhas[0]
            dicio['nome'] = linhas[1]
            dicio['idade'] = linhas[2]
            dicio['sexo'] = linhas[3]
            dicio['email'] = linhas[4]
            dicio['tel'] = linhas[5]

            
            lista.append(dicio)
        return lista


    def consulta (self,cliente):
        
        pass

a = Cadastro()

b = a.print()

print(b)