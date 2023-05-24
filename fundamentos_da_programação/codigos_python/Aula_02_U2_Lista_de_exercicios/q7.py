listaA=[1,2,3,4,5,6,7,8,9,10]
listaB=[1,2,3,4,5,6,7,8,9,10]
listaC = [elemA + elemB for elemA, elemB in zip(listaA, listaB)]

print(&#39;A soma de lista A&#39;,listaA,&#39;mais a soma da lista B&#39;,listaB,&#39;e
igual a:{}&#39;.format(listaC))