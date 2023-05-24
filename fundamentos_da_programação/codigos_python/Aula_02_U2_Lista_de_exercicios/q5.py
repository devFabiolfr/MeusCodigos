lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista)
listapar = []
listaimpar = []
for valor in lista:
  if valor % 2 == 0:
    listapar.append(valor)
  else:
    listaimpar.append(valor)
print(listapar)
print(listaimpar)