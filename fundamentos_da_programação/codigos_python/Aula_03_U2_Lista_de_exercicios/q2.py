# Time 1
insc1 = []
nome1 = []
sexo1 = []
idade1 = []
# Time 2
insc2 = []
nome2 = []
sexo2 = []
idade2 = []

for i in range (6):
insc1.append(i + 1)
nome1.append(input(&#39;Nome: &#39;))
idade1.append(int(input(&#39;Idade: &#39;)))
sexo1.append(input(&#39;Sexo: &#39;))
for j in range (6):

insc2.append(j + 7)
nome2.append(input(&#39;Nome: &#39;))
idade2.append(int(input(&#39;Idade: &#39;)))
sexo2.append(input(&#39;Sexo: &#39;))

# Imprimir equipe 1
print(&#39;Equipe 1:&#39;)
print(&#39;INSCRIÇÃO NOME SEXO IDADE\n--------- ----
---- -----&#39;)
for k in range (6):
print(&#39;-- {:0&gt;2}{:^25}{} {}&#39;.format(insc1[k],
nome1[k].strip().title(), sexo1[k].strip().upper(), idade1[k]))
print(&#39;Média de idades da equipe: {:.2f}\n\n&#39;.format(sum(idade1) / 6))
# Imprimir equipe 2
print(&#39;Equipe 2:&#39;)
print(&#39;INSCRIÇÃO NOME SEXO IDADE\n--------- ----
---- -----&#39;)
for l in range (6):
print(&#39;-- {:0&gt;2}{:^25}{} {}&#39;. format(insc2[l],
nome2[l].strip().title(), sexo2[l].strip().upper(), idade2[l]))
print(&#39;Média de idades da equipe: {:.2f}&#39;.format(sum(idade2) / 6))