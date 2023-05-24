#QUESTÃO 3
#Faça um algoritmo em Python, utilizando o comando PARA, que imprima todos os números pares existentes entre 1.000 e 1.200.

print(' Números Pares Entre 1.000 e 1.200')
n = 0
for n in range(1001, 1201):
    if n % 2 == 0:
        print(n, end=' ')
print('FIM')