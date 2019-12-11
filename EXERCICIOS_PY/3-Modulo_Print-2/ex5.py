#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha

name = 'George Gabriel Pereira da Silva'
link_linkedin = 'www.linkedin.com/georgegabriel'
link_git = 'https://github.com/Geo-Gabriel'
a = '===---'
b = '#---#---'

print(f'{a * 12}')
print(f'GEORGE GABRIEL - Estudante - Programador - 18 anos - Solteiro')
print(a * 12)
print (f'''--> Bem vindo ao meu perfil blablablablablablablabla \n Espero que meus posts te façam feliz porque vc merece :) \n\n 
Aqui você encontrará os meios onde poderá entrar em contato com minha pessoa :)\n \nLINKEDIN: {link_git} \nGITHUB: {link_git}\n\n''')