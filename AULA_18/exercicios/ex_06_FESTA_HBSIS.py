# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def ler_cadastro():
    arquivo = open('cadastro.txt','r')
    lista = []
    for pessoas in arquivo:
        pessoas = pessoas.strip().split(';')
        dicio = {'codigo':pessoas[0], 'nome': pessoas[1], 'sexo': pessoas[2], 'idade': pessoas[3]}
        lista.append(dicio)
    arquivo.close()
    return lista

def lista_festa (lista_entrada):
    lista_homens = []
    lista_mulheres = []
    for pessoas in lista_entrada:
        if int(pessoas['idade']) >= 18:
            if pessoas ['sexo'] == 'f':
                lista_mulheres.append(pessoas)
            else:
                lista_homens.append(pessoas)
        salvar(lista_homens, 'homens')
        salvar(lista_mulheres, 'mulheres')


def salvar (lista,nome):
    arquivo = open('nome.txt', 'a')
    for pessoas in lista:
        texto = f"{pessoas['codigo']} ; {pessoas['nome']}, {pessoas['sexo'], {pessoas['idade']}}"
        arquivo.write(texto)

    arquivo.close()

def consulta(lista_consulta_funcao, numero):
    for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['codigo']) == numero:
            if int(lista_consulta['idade']) >= 18:
                if lista_consulta['sexo'] == 'f':
                    print(f"nome: {lista_consulta['nome']} valor ingresso 15 R$")
                else:
                    print(f"Nome: {lista_consulta['nome']} valor ingressp 35 R$")
            else:
                print('Não pode entrar')
                