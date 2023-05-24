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
# Os códigos são feitos por palavras com
# 6 caracteres formadas por duas letras
# maiúsculas (especialidade) e 4 números
# (identificação).

# Diferenciação:
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
freeUseList = []     # Free use
codesList = []       # Lista de códigos utilizados
cpfList = []         # Lista de CPFs

answersList = ['S', 's', 'N', 'n']
espListSig = ['CG', 'NU', 'FN', 'FS', 'OT']
espList = ['Clínico Geral', 'Nutricionista', 'Fonoaudiólogo', 'Fisioterapeuta', 'Odontólogo']
espVal = [0.00, 0.00, 0.00, 0.00, 0.00]


# Vars
caixa = qAtPrimConsul = valorOdonto = qtdConsulRet = descConvTot = 0  
 




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

    print('\n ~~Sugestão para teste: "{}"'.format(sugestao))


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


    # Idade
    idade = int(input('\nIdade: '))

    while (idade < 0) or (idade > 150):
        print('\033[1;31;40m"{}" não é uma idade válida. Tente novamente\n'.format(idade))
        idade = input('\033[0;37;40mIdade: ')


    # Possui convênio?
    convCheck = input('\nPossui convênio (s/n): ')

    while convCheck in answersList == False:
        print('\033[1;31;40m"{}" não é uma resposta válida. Tente novamente\n'.format(convCheck))
        convCheck = input('\033[0;37;40mPossui convênio (s/n): ')


    # 1ª vez ou retorno
    timeCheck = input('\nConsulta de retorno (s/n): ')
    
    while timeCheck in answersList == False:
        print('\033[1;31;40m"{}" não é uma resposta válida. Tente novamente\n'.format(timeCheck))
        timeCheck = input('\033[0;37;40mPossui convênio (s/n): ')


    # Atribuir o valor da consulta
    if (timeCheck == 'N') or (timeCheck == 'n'):  # Pago
        qAtPrimConsul += 1 
        
        if code[0:2] == 'NU':
            preco = 150.00

        elif code[0:2] == 'FS':
            preco = 150.00

        elif code[0:2] == 'FN':
            preco = 200.00

        elif code[0:2] == 'OT':
            preco = 200.00
            valorOdonto += preco

        else:
            preco = 250.00
    

        # Atribuir desconto do convênio
        if (convCheck == 'S') or (convCheck == 's'):
            descConvTot += preco * 0.75
            preco *= 0.25

    else:  # Free use (Consulta de retorno)
        preco = 0
        qtdConsulRet += 1
        freeUseList.append(nome.title().strip())
   

    # Atribuir especialidade
    if code[0:2] == 'NU':
        espVal[1] += preco
        esp = 'Nutricionista'

    elif code[0:2] == 'FS':
        espVal[3] += preco
        esp = 'Fisioterapeuta'

    elif code[0:2] == 'FN':
        espVal[2] += preco
        esp = 'Fonoaudiólogo'

    elif code[0:2] == 'OT':
        valorOdonto += preco
        espVal[4] += preco
        esp = 'Odontólogo'

    else:
        espVal[0] += preco
        esp = 'Clínico Geral'
     

    caixa += preco


    # Tela de confirmação
    print('----------------------------------\n|  \/  Clínica Vida e Saúde  \/  |\n----------------------------------\n Recepção \n\n\nConfirmado\n-----------\n')  
    print('Nome: {}\nCPF: {}\n\nEspecialista: {}\n >Total: R${:.2f}\n'.format(nome.title().strip(), cpfFormatted, esp, preco))
    print('\033[1;32;40mRegistrado com sucesso ✔\n\n\n\n\n\n\n')


  

#///////////////////////////


# Cálculos

# Letra E
perConsulRet = (qtdConsulRet * 100) / len(cpfList)
  

#///////////////////////////


# Respostas
print('\n\n\n >Resultados:\n')

# Letra A ✔
print('A) Quantidade de atendimentos de primeira consulta: {}'.format(qAtPrimConsul))


# Letra B ✔
print('\nB) O valor total arrecadado pela clínica com o especialista em odontologia foi: R${:.2f}'.format(valorOdonto))


# Letra C ✔
print('\nC) Relação de pacientes que não pagaram consulta por ser uma consulta de retorno:')
print('NOME\n----')
for j in range(len(freeUseList)):
  print('- {}'.format(freeUseList[j]))
if len(freeUseList) == 0:
  print('- Vazio')


# Letra D ✔
print('\nD) Valor total de descontos por convênio foi: R${:.2f}'.format(descConvTot))


# Letra E ✔
print('\nE) Percentual de consultas de retorno: {:.1f}%'.format(perConsulRet))


# Letra F ✔
print('\nF) O valor total arrecadado pela clínica por especialista foi:')
print('ESPECIALISTA     PARTE NO VALOR\n------------     ------------------')
for k in range(5):
  print('- {:<31}R${:.2f}'.format(espList[k], espVal[k]))
print('-------\nTotal: R${:.2f}'.format(caixa))
