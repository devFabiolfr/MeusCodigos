# /////////////////////////////////////
# ///////////// ANOTAÇÕES /////////////
# /////////////////////////////////////


# PARTICIPANTES DO GRUPO 

# Wolney José Freitas de Oliveira
# Fabio Luiz da Fonseca Rocha
# Pedro Moreira Guerra de Almeida
# Luiz felipe nascimento gomez
# José Sávio Almeida Ribeiro



# ||||||||||||||| IMPORTANTE |||||||||||||||
# -------- Funcionamento do programa -------

# IDENTIFICAÇÃO DE CÓDIGOS
# Os códigos são formados por palavras com
# 6 caracteres formadas por duas letras
# maiúsculas (especialidade) e 4 números
# (identificação).

# Exemplos:
# CG0000  -  Clínico Geral
# NU0000  -  Nutricionista
# FN0000  -  Fonoaudiólogo
# FS0000  -  Fisioterapeuta
# OT0000  -  Odontólogo

# Uma vez utilizado, um código não poderá ser
# lido novamente, garantindo que cada paciente
# possua um código próprio.

# Para a facilitação de testes, um código aleatório
# será sugerido.





# /////////////////////////////////////
# /////////////// CÓDIGO //////////////
# /////////////////////////////////////
from random import randint


# Lists
namesList = []       # Lista de nomes
codesList = []       # Lista de códigos utilizados
agesList = []        # Lista de idades
cpfList = []         # Lista de CPFs

answersList = ['S', 's', 'N', 'n']
espListSig = ['CG', 'NU', 'FN', 'FS', 'OT']
espList = ['Clínico Geral', 'Nutricionista', 'Fonoaudiólogo', 'Fisioterapeuta', 'Odontólogo']
espQtd = [0, 0, 0, 0, 0]
b=[]
# Vars
caixa = 0            # Valor arrecadado pela clínica





print(r'\\\ Para finalizar, digite "-1"')


# Inserir dados do paciente
while True:
    print('\033[0;37;40m\n----------------------------------\n|  \/  Clínica Vida e Saúde  \/  |\n----------------------------------\n Recepção \n\n\nNovo paciente\n--------------\n')

    # CPF
    cpf = int(input('CPF (Apenas os dígitos): '))
    if cpf == -1:
        break

    # Validar CPF
    while (cpf in cpfList) or (cpf > 99999999999):
        if cpf > 99999999999:
            print('\033[1;31;40mCPF inválido. Tente novamente\n')
            cpf = int(input('\033[0;37;40mCPF (Apenas os dígitos): '))
        else:
            print('\033[1;31;40mCPF já cadastrado. Tente novamente\n')
            cpf = int(input('\033[0;37;40mCPF (Apenas os dígitos): '))    

    # Formatar CPF para 000.000.000-00
    cpfFormatStep1 = str(cpf)
    
    cpfFormatStep2 = (11 - len(cpfFormatStep1)) * '0' + str(cpfFormatStep1)

    cpfFormatted = cpfFormatStep2[:3] + '.' + cpfFormatStep2[3:6] + '.' + cpfFormatStep2[6:9] + '-' + cpfFormatStep2[9:]
    
    cpfList.append(cpfFormatted)

    # Sugerir um código para teste
    sugestao = str(espListSig[randint(0, 4)]) + str(randint(0, 9999))

    if len(sugestao) != 6:
        if len(sugestao) == 5:
            x = 2
        elif len(sugestao) == 4:
            x = 3
        else:
            x = 4    

        sugestao = sugestao[:2] + (x * '0') + sugestao[3:]

    while sugestao in codesList:
        sugestao = str(espListSig[randint(0, 4)]) + str(randint(0, 9999))
        if len(sugestao) != 6:
            if len(sugestao) == 5:
                x = 2
            elif len(sugestao) == 4:
                x = 3
            else:
                x = 4

            sugestao = sugestao[:2] + (x * '0') + sugestao[3:]

    print('\n---Sugestão para teste: "{}"'.format(sugestao))

    # Código
    code = input('Código: ')

    if code != sugestao:
        # Conferir validade e se já foi cadastrado
        while (len(code) != 6) or ((code[0:2] != 'CG') and (code[0:2] != 'NU') and (code[0:2] != 'FN') and (code[0:2] != 'FS') and (code[0:2] != 'OT')) or (code[2:6].isnumeric() == False) or (code in codesList):
            if code in codesList:
                print('\033[1;31;40mCódigo já cadastrado. Tente novamente\n')
                code = input('\033[0;37;40mCódigo: ')

            else:    
                print('\033[1;31;40mCódigo inválido!! Tente novamente\n')
                code = input('\033[0;37;40mCódigo: ')
    
    codesList.append(code)

    # Nome
    nome = input('\nNome: ')
    namesList.append(nome.title().strip())

    # Idade
    idade = int(input('\nIdade: '))

    while (idade < 0) or (idade > 150):
        print('\033[1;31;40m"{}" não é uma idade válida. Tente novamente\n'.format(idade))
        idade = input('\033[0;37;40mIdade: ')

    agesList.append(idade)    

    # Possui convênio?
    convCheck = input('\nPossui convênio (s/n): ')

    while convCheck in answersList == False:
        print('\033[1;31;40m"{}" não é uma resposta válida. Tente novamente\n'.format(convCheck))
        convCheck = input('\033[0;37;40mPossui convênio (s/n): ')

    # Parte da Letra B
    if idade > 59 and ((convCheck == 'S') or (convCheck == 's')):
      b.append(nome.title().strip())


    # Atribuir especialidade e valor da consulta
    if code[0:2] == 'NU':
        preco = 150.00
        esp = 'Nutricionista'
        espQtd[1] += 1

    elif code[0:2] == 'FS':
        preco = 150.00
        esp = 'Fisioterapeuta'
        espQtd[3] += 1

    elif code[0:2] == 'FN':
        preco = 200.00
        esp = 'Fonoaudiólogo'
        espQtd[2] += 1

    elif code[0:2] == 'OT':
        preco = 200.00
        esp = 'Odontólogo'
        espQtd[4] += 1

    else:
        preco = 250.00  
        esp = 'Clínico Geral' 
        espQtd[0] += 1


    # Atribuir desconto
    if (convCheck == 'S') or (convCheck == 's'):
        preco *= 0.25

    caixa += preco


    # Tela de confirmação
    print('----------------------------------\n|  \/  Clínica Vida e Saúde  \/  |\n----------------------------------\n Recepção \n\n\nConfirmado\n-----------\n')  
    print('Nome: {}\nCPF: {}\n\nEspecialista: {}\n >Total: R${:.2f}\n'.format(namesList[len(namesList) - 1], cpfList[len(cpfList) - 1], esp, preco))
    print('\033[1;32;40mRegistrado com sucesso ✔\n\n\n\n\n\n\n')


  


# Respostas
# Letra A
print('\nA) Relação de especialistas e suas respectivas quantidades de atendimentos realizados no expediente:\n')
print('ESPECIALISTA     Q. DE ATENDIMENTOS\n------------     ------------------')
for j in range(5):
  print('- {:<31}{:0>2}'.format(espList[j], espQtd[j]))

# Letra B
print('\nB) Relação nominal dos clientes que possuem o convênio com a clínica e que tem mais de 59:\n')
print('NOME\n----')
for k in range(len(b)):
  print('- {}'.format(b[k]))

# Letra C
print('\nC) Percentual de clientes que realizaram procedimentos com um Fisioterapeuta: {:.1f}%'.format((espQtd[3] * 100) / sum(espQtd)))

# Letra D
print('\nD) Valor total arrecadado pela clínica no final do expediente: R${:.2f}'.format(caixa))
