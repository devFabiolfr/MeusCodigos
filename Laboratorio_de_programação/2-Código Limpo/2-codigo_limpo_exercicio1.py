#Exercício 1
try:
    # listas
    questoes = []
    respostas = []

    # laço para ler as questões e respectivas respostas
    qtd_questoes = int(input('Quantas questões possuem a prova? '))
    for i in range(qtd_questoes):
        questoes.append((input(f'Questão {i + 1}: ')))
        respostas.append((input(f'Resposta da Questão {i + 1}: ')))

    # laço para solicitar as respostas dos usuarios
    while True:

        nome = input('Nome do usuário: ')

        #laço pra solicitar as respostas do usuário
        resp_usuarios = []
        for i in range(len(questoes)):
            print(f'Questão {i+1}: {questoes[i]}')
            resp_usuarios.append(input(f'Resposta da questão {i+1}:'))

        #laço para validação das respostas do usuário e impressão do resultado
        acertos = 0
        erros = 0
        for i in range(len(questoes)):
            print(f'Usuário: {nome}')
            print('Resultado: ')
            if resp_usuarios[i] == respostas[i]:
                print(f'Questão {i+1}: Correta!')
                acertos += 1
            else:
                print(f'Questão {i+1}: Incorreta!')
                erros += 1
        print(f'Total: {acertos} acertos e {erros} erros.')

        #validação para sair do laço
        if input('Deseja sair? [SAIR]') == 'SAIR':
            break
except (ValueError, OverflowError):
    print('Ocorreu um erro!')