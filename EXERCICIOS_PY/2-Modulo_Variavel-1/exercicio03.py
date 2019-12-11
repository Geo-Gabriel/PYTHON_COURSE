#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro


titulo = 'Mentes extraordinárias - Como desenvolver todo o potencial do seu cérebro'
edicao = '1ª Edição'
autor = "Alberto Dell'Isola"
ano_pub = '2018'
print()
print('''       É importante salientar que a criatividade possui amplo 
destaque nas artes, na música, na ciência, nas grandes decober-
tas. O que teriam as pessoas que se sobressaíram nestes campos,
que as demais não possuem? Será um talento inato?\n
        Como dito no início deste capítulo, não há de se falar em
"dom" ou "talento" quando trata de criatividade. O que as pessoas
que se destacam no campo criativo possuem chama-se esforço
intelectual. Somente este trabalho é reiterado, é possível al-
cançar níveis mais profundos na criatividade humana.\n\n ''')

print(f'{titulo}\n{autor}, {edicao}, {ano_pub}')