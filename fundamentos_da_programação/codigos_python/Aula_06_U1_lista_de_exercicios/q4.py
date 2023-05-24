#QUESTÃO 4
s = 0
for a in range(500, 800, 2):
    s += a
g = 0
for a in range(500, 800):
    if a % 2 == 1:
        g += a
print('Soma:', s)
print('Soma:', g)
print('FIM')