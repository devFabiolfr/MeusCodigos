from random import randint
lista1 = []
lista2 = []
tam = int(input(&#39;Insira o tamanho das listas: &#39;))
for i in range(tam):
lista1.append(randint(0, 9))
lista2.append(randint(0, 9))
lista3 = lista1 + lista2
lista4 = lista1 + lista2 + lista3
tam1 = len(lista1)
tam2 = len(lista2)
print(&quot;Lista 3 original: {}\n&quot;.format(lista3))
while True:
tam3 = len(lista3)

print(
&quot; (1) Inserir um número aleatório na lista 3 \n (2) Remover o
último número da lista 3\n (3) Imprimir a soma dos números da lista 3\n
(4) Imprimir a quantidade de números existentes nas listas 1, 2 e 3\n
(5) Imprimir as três listas em ordem crescente\n (0) Finalizar o
programa\n&quot;)
numOp = int(input(&quot;Insira o número da operação que deseja realizar:
&quot;))
if numOp == 1:
lista3.append(randint(0, 9))
elif numOp == 2:
lista3.pop()
elif numOp == 3:
print(&quot;Soma dos números da lista 3: {}\n&quot;.format(sum(lista3)))
elif numOp == 4:
print(&quot;Quantidade de números: {}\n&quot;.format(tam1 + tam2 + tam3))
elif numOp == 5:
print(&quot;As três listas em ordem crescente:
{}\n&quot;.format(sorted(lista4)))
elif numOp == 0:
break
else:
print(&quot;Esse número não é válido!!!&quot;)
print(&quot;Lista 3 atual: {}\n&quot;.format(lista3))