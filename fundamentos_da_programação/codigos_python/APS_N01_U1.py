#Nomes do Grupo:
#Fabio Luizda Fonseca Rocha, Pedro Moreira Guerra de Almeida, José Sávio Almeida Ribeiro, Luiz Felipe Nascimento Gomes e Wolney José Freitas de Oliveira

pontos = 0
qCondutores = 0
somaPontos = 0

_20pontos = 0
_30pontos = 0
_40pontos = 0

por20 = 0
media = 0


while True:
    cnh = str(input("Insira o número da CNH: "))
    pontos = int(input("Insira a quantidade de pontos nessa CNH: "))
    infr = int(input("Insira a quantidade de infrações gravíssimas nessa CNH: "))
    maisUma = str(input("Deseja registrar mais um CNH? (s/n) "))


    somaPontos += pontos
    qCondutores += 1


    # Conferir os pontos
    if (pontos >= 40) and (infr == 0):
        _40pontos += 1

    elif (pontos >= 30) and (infr == 1):
        _30pontos += 1

    elif (pontos >= 20) and (infr >= 2):
        _20pontos += 1           
    
    if ((maisUma == "n") or (maisUma == "N")):
        break
    

# Letra B
por20 = (_20pontos * 100) / qCondutores

# Letra C
media = somaPontos / qCondutores


# Respostas
# Letra A
print('A) {} condutores tiveram sua CNH suspensa com 30 pontos'.format(_30pontos))

# Letra B
print('B) {}% dos condutores tiveram a sua CNH suspensa com 20 pontos'.format(por20))

# Letra C
print('C) Média da quantidade de pontos registrados:', media)