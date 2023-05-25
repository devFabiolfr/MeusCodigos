#programa
import funcoes

opcao = -1
while opcao != 0:
    print('Escolha o objeto que deseja calcular a área')
    print()
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Círculo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        lado_a = float(input('Entre com um lado do retângulo: '))
        lado_b = float(input('Entre com o outro lado do retângulo: '))
        area = Exercicio4.funcoes.retangulo(lado_a, lado_b)
        print('\nA área do retâgulo é: {0:.2f}'.format(area))
    elif (opcao == 2):
        lado = float(input('Entre com a base do triângulo: '))
        altura = float(input('Entre com a altura do triângulo: '))
        area = Exercicio4.funcoes.triangulo(lado, altura)
        print('\nA área do triângulo é: {0:.2f}'.format(area))
    elif (opcao == 3):
        raio = float(input('Entre com o raio do cículo: '))
        area = Exercicio4.funcoes.circulo(raio)
        print('\nA área do círculo é: {0:.2f}'.format(area))
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()
print('Volte a qualquer hora')