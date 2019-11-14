# AULA 7 - 14- 11-2019
# DICIONARIOS

'''lista = []
dicionario = {'nome':'George', 'sobrenome':'gabriel'} # Para cada dado eu dou um significado 
print(dicionario)
print(dicionario['sobrenome'])'''


nome = 'George'
lista_notas = [20,30,10,50]
media = sum(lista_notas) / len(lista_notas)
situacao = 'Reprovado'

if media >= 7:
    situacao = 'Aprovado'

dicionario_alunos = {'Nome': input('Nome: '), 'Lista_notas': lista_notas, 'média': media, 'situacao': situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['situacao']}")