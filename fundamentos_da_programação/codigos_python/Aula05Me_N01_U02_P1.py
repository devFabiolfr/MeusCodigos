#Nomes do Grupo:
#Pedro Moreira Guerra de Almeida
#Fabio Luiz da Fonseca Rocha
#José Sávio Almeida Ribeiro
#Wolney José Freitas de Oliveira
#Luiz felipe nascimento gomez

nomes = []
idades = []
precos = []
descontos = []

q10prc = 0
n = 0 



print("PARA PARAR PROCESSO DIGITE '0'.\n")

while True:
  n += 1

  nome = (input("Insira o nome do {}º cliente: ".format(n)))

  if nome == "0":
    break

  idade = (int(input("Insira a idade do {}º cliente: ".format(n))))

  while (idade < 0) or (idade > 150):
    print('{} não é uma idade válida!!\n'.format(idade))
    idade = int(input('Insira a idade do {}º cliente: ').format(n))


  if idade <= 5:
    preco = 18.0
    q10prc += 1

  elif idade <= 12: 
    preco = 18.4

  elif idade <= 25:
    preco = 19.0

  elif idade > 60:
    preco = 17.0

  else:
      preco = 20.0  
     

  
  nomes.append(nome.strip().title())
  idades.append(idade)
  precos.append(preco)


  if preco != 20:
      descontos.append(preco)
 

# Letra A ✔
print('A)')
print('NOME               IDADE       VALOR')
print('----               -----       -----')
for i in range(len(nomes)):
  print('{:<21}{:>3}        R${}'.format(nomes[i], idades[i], precos[i]))


# Letra B ✔
print("\nB) {} pessoas tiveram desconto na entrada\n".format(len(descontos)))


# Letra C ✔
print("C) {}% das pessoas tiveram desconto de 10%\n".format((100 * q10prc) / len(nomes)))


# Letra D ✔
print('D)')
print('NOME               IDADE       VALOR')
print('----               -----       -----')
for j in range(len(nomes)):
    if idades[j] >= 60:
        print('{:<21}{:>3}        R${}'.format(nomes[j], idades[j], precos[j]))



# Letra E ✔ 
print('\nE) Média do valor de descontos aplicados: {}'.format(sum(descontos) / len(descontos)))

