listaA=[1,2,3,4,5,6,7,8,9,10]
listaB=[1,2,3,4,5,6,7,8,9,10]
listaC = [elemA + elemB for elemA, elemB in zip(listaA, listaB)]

print('A soma de lista, listaA,mais a soma da lista,listaB, e igual a:',{}.format(listaC))