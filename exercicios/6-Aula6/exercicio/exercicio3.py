#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

lista_alunos_notas = []


for i in range(0,2):
    lista_alunos = []
    lista_alunos.append(input(f'Digite o nome do aluno {i+1}:'))
    lista_notas = []
    for n in range(0,4):
        lista_notas.append( float(input(f'Digite a nota {n+1}:')) )  
    lista_alunos.append(lista_notas)
    lista_alunos_notas.append(lista_alunos)

for aluno_nota in lista_alunos_notas:    
    notas_aluno = aluno_nota[1]
    media = (notas_aluno[0]+ notas_aluno[1] + notas_aluno[2]+ notas_aluno[3])/4
    resultado = 'Reprovado'
    if media >=7:
        resultado = 'Aprovado'
    print(f'Aluno: {aluno_nota[0]} - média={media} - Resultado: {resultado}')

print(lista_alunos_notas)
