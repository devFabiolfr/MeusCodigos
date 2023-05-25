#Exercício 1
#funcoes:
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

def listar_cadeiras_disponiveis(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == False:
                disponiveis.append(j+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []

def excluir_reserva(matriz, fila, cadeira):
    matriz[fila-1][cadeira-1] = False
    return matriz

#programa
from Exercicio4 import funcoes

FILAS = 25
CADEIRAS = 40
lugares = funcoes.criação_matriz(FILAS, CADEIRAS)

#menu
opcao = 1
while opcao != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Consultar reservas')
    print('2 - Cadastrar reserva')
    print('3 - Listas cadeiras disponíveis')
    print('4 - Excluir reserva')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        funcoes.impressão_matriz(lugares)
    elif (opcao == 2):
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_cadeira = int(input('Cadeira: '))
            assert 1 <= reserva_cadeira <= CADEIRAS

            if funcoes.consulta_reserva_cadeira(lugares, reserva_fila, reserva_cadeira):
                print('Essa cadeira já está reservada!')
            else:
                lugares = funcoes.reserva_cadeira(lugares, reserva_fila, reserva_cadeira)
                print(f'Cadeira [{reserva_fila}][{reserva_cadeira}] reservada!')
        except AssertionError:
            print('Informação inválida')
    elif (opcao == 3):
        funcoes.listar_cadeiras_disponiveis(lugares)
    elif (opcao == 4):
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_cadeira = int(input('Cadeira: '))
            assert 1 <= reserva_cadeira <= CADEIRAS

            if funcoes.consulta_reserva_cadeira(lugares, reserva_fila, reserva_cadeira) == False:
                print('Essa cadeira já está disponível!')
            else:
                lugares = funcoes.excluir_reserva(lugares, reserva_fila, reserva_cadeira)
                print(f'Reserva da cadeira [{reserva_fila}][{reserva_cadeira}] excluída!')
        except AssertionError:
            print('Informação inválida')
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()





#Exercício2
#funcoes:
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

def listar_cadeiras_disponiveis(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == False:
                disponiveis.append(j+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []

def excluir_reserva(matriz, fila, cadeira):
    matriz[fila-1][cadeira-1] = False
    return matriz


def cadastrar_cliente(dic, nome):
    dic[nome] = '0'
    return dic

def consulta_reserva_cliente(dic, nome):
    return dic.get(nome)

def reserva_cadeira_cliente(dic, nome, fila, cadeira):
    if dic.get(nome) == None:
        dic[nome] = 'Fila ' + fila + ' Cadeira ' + cadeira
    else:
        del dic[nome]
        dic[nome] = 'Fila ' + str(fila) + ' Cadeira ' + str(cadeira)


#programa:
from Exercicio5 import funcoes

FILAS = 25
CADEIRAS = 40
lugares = funcoes.criação_matriz(FILAS, CADEIRAS)
clientes = {}

#menu
opcao = 1
while opcao != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Consultar reservas')
    print('2 - Cadastrar reserva para o cliente')
    print('3 - Listas cadeiras disponíveis')
    print('4 - Excluir reserva')
    print('5 - Cadastrar cliente')
    print('6 - Consultar reserva do cliente')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        funcoes.impressão_matriz(lugares)
    elif (opcao == 2):
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_cadeira = int(input('Cadeira: '))
            assert 1 <= reserva_cadeira <= CADEIRAS

            if funcoes.consulta_reserva_cadeira(lugares, reserva_fila, reserva_cadeira):
                print('Essa cadeira já está reservada!')
            else:
                nome = input('Nome do Cliente: ')
                reserva = funcoes.consulta_reserva_cliente(clientes, nome)
                if reserva == None:
                    print('Cliente não cadastrado!')
                else:
                    funcoes.reserva_cadeira_cliente(clientes, nome, reserva_fila, reserva_cadeira)
                    lugares = funcoes.reserva_cadeira(lugares, reserva_fila, reserva_cadeira)
                    print(f'Cadeira [{reserva_fila}][{reserva_cadeira}] reservada para o cliente {nome}!')
        except AssertionError:
            print('Informação inválida')
    elif (opcao == 3):
        funcoes.listar_cadeiras_disponiveis(lugares)
    elif (opcao == 4):
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_cadeira = int(input('Cadeira: '))
            assert 1 <= reserva_cadeira <= CADEIRAS

            if funcoes.consulta_reserva_cadeira(lugares, reserva_fila, reserva_cadeira) == False:
                print('Essa cadeira já está disponível!')
            else:
                lugares = funcoes.excluir_reserva(lugares, reserva_fila, reserva_cadeira)
                print(f'Reserva da cadeira [{reserva_fila}][{reserva_cadeira}] excluída!')
        except AssertionError:
            print('Informação inválida')
    elif (opcao == 5):
        nome = input('Nome do Cliente: ')
        funcoes.cadastrar_cliente(clientes, nome)
    elif (opcao == 6):
        nome = input('Nome do Cliente: ')
        reserva = funcoes.consulta_reserva_cliente(clientes, nome)
        if reserva == None:
            print('Cliente não cadastrado!')
        else:
            if reserva != '0':
                print(f'Cliente: {nome} - Reserva: {reserva}')
            else:
                print('Cliente não possui reserva!')
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()

