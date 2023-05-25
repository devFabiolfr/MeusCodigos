medias = []
numAl = 0
for i in range(10):
numAl += 1
somaNotas = 0
a = 0
print(&#39;Notas do(a) aluno(a) {}&#39;.format(numAl))
for a in range(4):
nota = float(input(&#39;Digite a {}ª nota: &#39;.format(a + 1)))
somaNotas += nota
mediaInd = somaNotas / 4
medias.append(mediaInd)

print(&#39;Alunos com média maior ou igual a 7:\n&#39;)
for b in range(len(medias)):
if medias[b] &gt;= 7:
print(&#39;- Aluno {}&#39;.format(b + 1))