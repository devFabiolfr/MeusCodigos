from random import randint
numeros = []
surpre1 = []
surpre2 = []
resulta = []
# letra A
nDez = int(input('Quantidade de dezenas: '))
if nDez > 8000:
print('MAIS DE 8 MIL!? MAS ISSO É IMPOSSÍVEL!!\n')
elif (nDez > 18) or (nDez <= 8000):
print('{} patinhos foram passear... Opa... Esse número não dá
:/\n'.format(nDez))
while (nDez < 15) or (nDez > 18):
print('Digite uma quantidade válida (15-18)\n')
nDez = int(input('Quandidade de dezenas: '))
# letra B
for i in range(nDez):
num = int(input('{}º número: '.format(i + 1)))
while (num < 1) or (num > 25):
print('Dezena inválida!!! Digite novamente\n')
num = int(input('{}º número: '.format(i + 1)))
while num in numeros:
print('Número repetido!!! Digite novamente\n')
num = int(input('{}º número: '.format(i + 1)))
numeros.append(num)
# letra C
for j in range(18):
num1 = randint(1, 25)
num2 = randint(1, 25)