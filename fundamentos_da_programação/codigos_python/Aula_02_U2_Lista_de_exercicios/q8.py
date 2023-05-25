from random import randint
resultados = []
q1 = 0
q2 = 0
q3 = 0

q4 = 0
q5 = 0
q6 = 0
for i in range(10):
  resultados.append(randint(1, 6))
for a in range(len(resultados)):
  if resultados[a] == 1:
    q1 += 1
  elif resultados[a] == 2:
    q2 += 1
  elif resultados[a] == 3:
    q3 += 1
  elif resultados[a] == 4:
    q4 += 1
  elif resultados[a] == 5:
    q5 += 1
  else:
    q6 += 1
print('Quantidade de vezes cada valor foi obtido:')
print('1:',q1)
print('2:',q2)
print('3:',q3)
print('4:',q4)
print('5:',q5)
print('6:',q6)