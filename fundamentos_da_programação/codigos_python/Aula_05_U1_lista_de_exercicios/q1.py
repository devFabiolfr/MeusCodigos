#Questão 1
num1 = int(input("Digite um numero inteiro"))
num2 = int(input("Digite outro numero inteiro"))

iguais = num1 == num2
if (iguais):{
   print("os numeros são iguais")
}
else: {
  print("os numeros são diferentes")
}

#Questão 4
salario = int(input("Qual é o seu salario?"))
if (salario < 200):{
  print("Seu desconto do INSS é de 8%")
}
if (salario < 500):{
  print("Seu desconto do INSS é de 8.5%")
}
if (salario < 1000):{
  print("Seu desconto do INSS é de 9%")
}
if (salario >= 1000):{
  print("Seu desconto do INSS é de 9.5%")
}