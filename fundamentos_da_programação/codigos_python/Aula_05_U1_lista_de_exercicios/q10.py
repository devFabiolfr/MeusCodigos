
#QUESTÃO 10
numero1 = int(input("Digite um número 1 inteiro: "))
numero2 = int(input("Digite outro número 2 inteiro: "))
numero3 = int(input("Digite um número 3 inteiro: "))
soma =  numero1 + numero2 + numero3
print("soma dos númeroa é: ", soma)
produto = numero1 * numero2 * numero3
print("o produto dos númeroa é: ", produto)
if numero1 < numero2 < numero3 :
    print('número1 é o maior')
elif numero1 < numero2 > numero3 :
    print('número1 é o menor')