# Dias da semana
resSeg = 0
resTer = 0
resQua = 0
resQui = 0
resSex = 0

resSegTer = 0

nVeiculos = int(input("Digite a quantidade de veículos: "))

for i in range (1, nVeiculos + 1):
    placaVeic = int(input("Digite a placa do {}º veículo (Ex: 0000): ".format(i)))

    # Não aceitar números incompatíveis
    while (placaVeic < 1) or (placaVeic > 9999):
        print("DIGITE UM NÚMERO VÁLIDO!!")
        placaVeic = int(input("Digite a placa do {}º veículo (Ex: 0000): ".format(i)))

    # Ler o último número
    a = str(placaVeic)
    x = a[-1]

    # Guardar no dia
    if ((x == "1") or (x == "2")):
        resSeg += 1

    if ((x == "3") or (x == "4")):
        resTer += 1

    if ((x == "5") or (x == "6")):
        resQua += 1

    if ((x == "7") or (x == "8")):
        resQui += 1

    if ((x == "9") or (x == "0")):
        resSex += 1

    # Letra A
    resSegTer = resSeg + resTer

    # Letra B
    porSex = (resSex * 100) / nVeiculos

    # Letra C
    if ((resSeg > resTer) and (resSeg > resQua) and (resSeg > resQui) and (resSeg > resSex)):
        maiorRes = "Segunda-feira"

    elif ((resTer > resQua) and (resTer > resQui) and (resTer > resSex)):
        maiorRes = "Terça-feira"

    elif ((resQua > resQui) and (resQua > resSex)):
        maiorRes = "Quarta-feira"

    elif resQui > resSex:
        maiorRes = "Quinta-feira"

    else:
        maiorRes = "Sexta-feira"

print('A) {}\nB) {}%\nC) {}'.format(resSegTer, porSex, maiorRes))