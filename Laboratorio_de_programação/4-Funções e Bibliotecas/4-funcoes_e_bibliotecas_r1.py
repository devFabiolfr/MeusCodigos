#Exercício 1
def converteHora(hora24, minuto24):
    if (hora24 > 23) or (hora24 < 0) or (minuto24 < 0) or (minuto24 > 59):
        return None

    if (hora24 < 12):
        if (hora24 == 0):
            hora24 = 12
        return '%02d:%02d AM' % (hora24, minuto24)

    if (hora24 > 12):
        hora24 -= 12
    return '%02d:%02d PM' % (hora24, minuto24)


def impressaoHora(horaMin):
    print(f'{horaMin[0:2]}:{horaMin[3:5]}')

# Entrada de dados
continuar = 'S'
while (continuar == 'S'):
    hora = int(input('Informe o valor da hora: '))
    minuto = int(input('Informe o valor dos minutos: '))

    horaConvert = converteHora(hora, minuto)
    if horaConvert == None:
        print('Hora é inválida')
    else:
        impressaoHora(horaConvert)


    continuar = input('Deseja continuar (S/N): ').upper()