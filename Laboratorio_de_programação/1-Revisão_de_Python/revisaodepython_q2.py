#Exercício 2
import random

numero = int(input("Quantas dezenas pretende apostar? (Entre 15 e 18) "))
a=0
if (numero<15 or numero>18):
    a = 1
while a:
    numero = int(input("Insira um número entre 15 e 18 "))
    a = 0
    if (numero<15 or numero>18):
        a = 1
aposta = []
for i in range(numero):
    valor = int(input(str(i)+" Insira o valor para apostar (individualmente) "))
    if valor in aposta:
        frase = "valor "+str(valor)+" já inserido. Favor inserir um diferente: "
        valor = int(input(frase))
    if (valor<1 or valor>25):
        valor = int(input("Dezena inválida. Insira um valor entre 1 e 25 "))
    aposta.append(valor)
import random
supresinha1 = random.sample(range(1, 26), 18)
supresinha2 = random.sample(range(1, 26), 18)
jogo = random.sample(range(1, 26), 15)
print("Aposta 1:")
print(sorted(aposta))
print("\n Surpresinha 1:")
print(sorted(supresinha1))
print("\n Surpresinha 2:")
print(sorted(supresinha2))
print("\n Resultado LOTOFACIL:")
print(sorted(jogo))
print("\n Dezenas acertadas na Aposta1:")
print(len(list(set(aposta).intersection(jogo))))
print("\n Dezenas acertadas na Surpresinha 1:")
print(len(list(set(supresinha1).intersection(jogo))))
print("\n Dezenas acertadas na Surpresinha 2:")
print(len(list(set(supresinha2).intersection(jogo))))