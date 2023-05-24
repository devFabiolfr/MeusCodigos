#Nomes do Grupo: Fabio_Luiz da Fonseca Rocha_if_José Sávio Almeida_if_Wolney_José_Freitas_de_Oliveira_if_Pedro_Moreira_Guerra_de_Almeida_if_Luiz_Felipe_Nascimento_Gomes
# Montantes
receitaProdutos = 0
receitaFrete = 0

# Letras A e B
maiorValor = 0
menorValor = 9999999999

while True:
    subTotal = 0
    valorTotal = 0

    cpf = str(input("Insira o CPF do cliente: "))
    
    if cpf == "-1":
        break

    while True:
        codigo = int(input("Insira o código do pedido: "))

        if codigo == -1:
            break
        
        while (codigo < 100) or (codigo > 105):
          print("'{}' não é um código válido \n".format(codigo))
          codigo = int(input('Insira o código do pedido: '))

        qnt = int(input("Insira a quantidade desejada desse pedido: "))

        if codigo == 100:
            subTotal += 4.20 * qnt
        
        elif codigo == 101:
            subTotal += 7.30 * qnt
        
        elif codigo == 102:
            subTotal += 8.50 * qnt
        
        elif codigo == 103:
            subTotal += 9.20 * qnt
        
        elif codigo == 104:
            subTotal += 10.30 * qnt
        
        else:
            subTotal += 8.00 * qnt


        receitaProdutos += subTotal   
        

    frete = int(input("Insira o frete desse pedido: "))
    receitaFrete += frete

    valorTotal = subTotal + frete

    # Letra A (Calculo)
    if valorTotal > maiorValor:
      maiorValor = valorTotal

    # Letra B (Calculo)
    if valorTotal < menorValor:
      menorValor = valorTotal  


# Letra C (Calculo)
receitaMotoboy = receitaFrete - (receitaFrete * 40/100)

# Letra D (Calculo)
receitaProprietario = receitaProdutos + (receitaFrete - (receitaFrete * 60/100))



# Respostas
print('\n \nRespostas: \n')
# Letra A
print('A) O maior valor recebido neste expediente foi de R${:.2f}'.format(maiorValor))

# Letra B
print('B) O menor valor recebido neste expediente foi de R${:.2f}'.format(menorValor))

# Letra C
print('C) O motoboy recebeu o valor de R${:.2f} no final deste expediente'.format(receitaMotoboy))

# Letra D
print('D) O proprietário recebeu o montante de R${:.2f} no final deste expediente'.format(receitaProprietario))