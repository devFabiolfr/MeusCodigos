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