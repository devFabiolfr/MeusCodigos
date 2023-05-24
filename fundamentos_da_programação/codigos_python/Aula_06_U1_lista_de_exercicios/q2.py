
#QUESTÃO 2
ordem = input("Digite C para imprimir os números em ordem crescente ou D para imprimir em ordem decrescente: ")
if ordem == "C":
    for i in range (30,51, 1):
        print (i)
elif ordem == "D":
    for i in range (50,29,-1):
        print (i)