#Exercício 2
try:
    palavra = 'banana'
    letras = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False
    erros = 0

    #impressão das letras para a forca
    print(letras)

    #laço para solicitar as letras ao usuário e validar os acertos e erros
    while not enforcou and not acertou:
        chute = input('Qual a letra? ')
        if chute in palavra:
            posicao = 0
            for letra in palavra:
                if chute.upper() == letra.upper():
                    letras[posicao] = chute
                posicao += 1
        else:
            erros += 1

        #valida se o usuário enforcou, ou seja, erro 3 vezes
        if erros == 3:
            enforcou = True
            print('Você excedeu o limite te tentativas!')
        #validar se o usuário acertou todas as letras
        if '_' not in letras:
            acertou = True
            print('Você acertou!')

        print(letras)

except (ValueError, OverflowError):
    print('Ocorreu um erro!')