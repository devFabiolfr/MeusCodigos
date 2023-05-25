#Fabio Luizda Fonseca Rocha, Pedro Moreira Guerra de Almeida, José Sávio Almeida Ribeiro, Luiz Felipe Nascimento Gomes e Wolney José Freitas de Oliveira


qEstados = 0
numCasosTotal = 0
varPrim = 1
numObitosAnterior = 211000000

while True:
    codigo = int(input("Digite o código do estado: "))

    if codigo == -1:
        break

    nomeEstado = str(input("Digite o nome do estado: "))
    numCasos = int(input("Digite o número de casos no estado: "))
    numObitos = int(input("Digite o número de óbitos no estado: "))
    
    # Não ler um número maior q 211 mi
    while numObitos > 211000000:
        print("O BRASIL TEM 211 Mi HABITANTES")
        numObitos = int(input("Digite o número de óbitos no estado: "))

    # Coisas pra letra B
    if numObitos < numObitosAnterior:
        numObitosAnterior = numObitos
        estMenCas = str(nomeEstado)
    
    # Coisas pra letra C
    if varPrim == 1:
        numCasosPrimE = numCasos
        varPrim = 0

    qEstados += 1
    numCasosTotal += numCasos
 

# Letra A
media = numCasosTotal / qEstados
print('A)', media)

# Letra B
print('B)', estMenCas)

# Letra C
porPrimE = (numCasosPrimE * 100) / numCasosTotal
print('C) {}%'.format(porPrimE))
