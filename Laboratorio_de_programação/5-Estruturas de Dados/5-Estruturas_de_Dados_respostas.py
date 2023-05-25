#Exercício 1
#funcoes.py
def maior_temp(x, y):
    if x[1] == y[1]:
        if x[0] > y[0]:
            return x
        else:
            return y
    else:
        if x[1] == 'F':
            x_convertido = (x[0]-32)/1.8
        else:
            x_convertido = 1.8*x[0]+32
        if x_convertido > y[0]:
            return x
        else:
            return y


#principal.py
from Exercicio1 import Funcoes

MSG_QUANT = 'Quantos graus? '
MSG_ESCALA = 'Qual a escala (C/F)? '
temp1 = float(input(MSG_QUANT))
escala1 = input(MSG_ESCALA)
temp2 = float(input(MSG_QUANT))
escala2 = input(MSG_ESCALA)
print(f'A maior temperatura é: ', Funcoes.maior_temp((temp1, escala1), (temp2, escala2)))



#Exercício 2
#funcoes.py
def particula_menor_probab(particulas):
    chave_menor = []
    valor_menor = 0
    for chave, valor in particulas.items():
        if valor_menor == 0:
            valor_menor = valor
            chave_menor.append(chave)
        elif valor == valor_menor:
            chave_menor.append(chave)
        elif valor < valor_menor:
            chave_menor = [chave]
            valor_menor = valor
    return chave_menor


#principal.py
from Exercicio2 import Funcoes

dic = {}
entrada = ''
while True:

    try:
        while True:
            nome_part = input('Nome da partícula: ')
            probab = float(input('Prababilidade: '))

            lstV = dic.values()
            if sum(lstV) + probab > 1:
                print('A soma das probabilidades é maior que 100%! Digite novamente.')
                entrada = input('Deseja inserir mais itens? [S/N] ')
                break

            dic[nome_part] = probab

            entrada = input('Deseja inserir mais itens? [S/N] ')
            if entrada == 'N':
                break
    except ValueError:
        print('Informe um número de probabilidade válido')

    if entrada == 'N':
        break

print(Funcoes.particula_menor_probab(dic))


#Exercício 3
#funcoes.py
def criação_matriz(FILA, CADEIRA):
    matriz = []
    #criando a matriz com todas as posições falsas
    for i in range(FILA):
        linha = []
        for j in range(CADEIRA):
            linha.append(False)
        matriz.append(linha)
    return matriz


def impressão_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def consulta_reserva_cadeira(matriz, fila, cadeira):
    if matriz[fila-1][cadeira-1]:
        return True
    else:
        return False

def reserva_cadeira(matriz, fila, cadeira):
    matriz[fila-1][cadeira-1] = True
    return matriz


#principal.py
from Exercício3 import funcoes

FILAS = 25
CADEIRAS = 40
lugares = funcoes.criação_matriz(FILAS, CADEIRAS)
funcoes.impressão_matriz(lugares)
entrada = ''
while True:
    try:
        while True:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_cadeira = int(input('Cadeira: '))
            assert 1 <= reserva_cadeira <= CADEIRAS

            if funcoes.consulta_reserva_cadeira(lugares, reserva_fila, reserva_cadeira):
                print('Essa cadeira já está reservada!')
            else:
                lugares = funcoes.reserva_cadeira(lugares, reserva_fila, reserva_cadeira)
                print(f'Cadeira [{reserva_fila}][{reserva_cadeira}] reservada!')

            entrada = input('Nova reserva? [S/N] ')
            if entrada == 'N':
                break

    except AssertionError:
        print('Informação inválida')

    if entrada == 'N':