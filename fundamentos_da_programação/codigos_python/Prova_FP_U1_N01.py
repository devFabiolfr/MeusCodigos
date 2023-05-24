# Fabio Luizda Fonseca Rocha, Pedro Moreira Guerra de Almeida, José Sávio Almeida Ribeiro, Luiz Felipe Nascimento Gomes e Wolney José Freitas de Oliveira

pontos = 0

nSus = 0
_20pontos = 0
_30pontos = 0
_40pontos = 0

mulheres = 0
homens = 0
ehMulher = False
ehHomem = False

m_nSus = 0
h_40pontos = 0
m_pontosTotal = 0 

pontosAntes = 99999999999
pontosMaior = 0


while True:
    cnh = str(input("Insira o número da CNH: "))

    nome = str(input("Insira o nome do dono da CNH:  "))

    sexo = str(input("Insira o sexo do dono da CNH (M para mulher e H para homem):  "))
    
    # Conferir o sexo
    if (sexo == "m") or (sexo == "M"):
      mulheres += 1
      ehMulher = True
    if (sexo == "h") or (sexo == "H"):
      homens += 1
      ehHomem = True
    

    pontos = int(input("Insira a quantidade de pontos nessa CNH: "))
    
    # Declarar o condutor com a menor pontuação
    if pontos < pontosAntes:

        pontosAntes = pontos

        condMenorPontu = str(cnh)

    # Declarar a maior pontuação
    if pontos > pontosMaior:

      pontosMaior = pontos

      maiorPontu = str(nome)

      sexoMaior = str(sexo)


    infr = int(input("Insira a quantidade de infrações gravíssimas nessa CNH: "))


    maisUma = str(input("Deseja registrar mais um CNH? (s/n) "))


    if ehMulher == True:
      m_pontosTotal += pontos


    # Conferir os pontos
    if (pontos >= 40) and (infr == 0):
        _40pontos += 1
        if ehHomem == True:
            h_40pontos += 1

    elif (pontos >= 30) and (infr == 1):
        _30pontos += 1

    elif (pontos >= 20) and (infr >= 2):
        _20pontos += 1

    else:
      nSus += 1
      if ehMulher == True:
          m_nSus += 1

    # Resetar se h ou m
    ehMulher = False
    ehHomem = False

    if (maisUma == "n") or (maisUma == "N"):
        break


#Letra A
print('A) A quantidade de condutores do sexo feminino que não tiveram a CNH suspesa foi de {}'.format(m_nSus))

#Letra B
print('B) A média da quantidade de pontos registrados de condutores do sexo feminino é {}'.format(m_pontosTotal / mulheres))

#Letra C
por40 = (h_40pontos * 100) / homens

print('C) {}% dos condutores do sexo masculino tiveram a sua CNH suspensa com 40 pontos'.format(por40))

#Letra D
print('D) {} pessoas não tiveram a sua CNH suspensa'.format(nSus))

#Letra E
print('E) {}({}) possui a maior quantidade de pontos registrados'.format(maiorPontu, sexoMaior))

#Letra F
print('F)', condMenorPontu)