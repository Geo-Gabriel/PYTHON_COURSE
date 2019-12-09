#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


'''lista_alunos = []
lista_notas = []
lista_medias = []

for i in range (0,2):
    alun = input('Digite o nome do aluno: ')
    n1 = int(input('Digite a nota1 do aluno: '))
    n2 = int(input('Digite a nota2 do aluno: '))
    n3 = int(input('Digite a nota3 do aluno: '))
    n4 = int(input('Digite a nota4 do aluno: '))

    media = (n1 + n2 + n3 + n4) / 4

    if media >= 7:
        print('Aprovado com média {}'.format(media))
    else:
        print('Reprovado com média {}'.format(media))

    lista_notas.append(n1)
    lista_notas.append(n2)
    lista_notas.append(n3)
    lista_notas.append(n4)
    lista_medias.append((n1 + n2 + n3 + n4) / 4)
    lista_alunos.append(alun)


print(lista_alunos)
print(lista_notas)
print(lista_medias)'''

alunos = []
notas = []

a = 0
b = 1
c = 3
d = 4

for i in range (0,2):
    alunos.append(input(f'Digite nome aluno {i+1}: '))
    for j in range (0,4):
        notas.append(int(input(f'Digite a nota {j+1}:')))

for nomes in alunos:
    media = (notas[a] + notas[b] + notas[c] + notas[d]) / 4

    resultado = 'Reprovado'
    if media >= 7:
        print(resultado)

    print(f'Aluno: {nomes} - Media: {media} - Resultado: {resultado}')

    a += 4
    b += 4
    c += 4
    d += 4