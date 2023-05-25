#Exercício 1
import random

#função para sortear 6 números
def sortear():
    lista = []
    while len(lista) < 6:
        sort = random.randint(1, 60)
        if lista.count(sort) == 0:
            lista.append(sort)
    lista.sort()
    return lista

#programa principal
entrada = input('Deseja sortear os números da mega-sena? [S/N]')
if entrada == 'S':
    print(sortear())
else:
    print('FIM')
