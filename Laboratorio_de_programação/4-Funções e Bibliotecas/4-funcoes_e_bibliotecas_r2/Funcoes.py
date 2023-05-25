#Exercício 3
#Funções.py
def é_par_ou_impar(numero):
    if numero % 2 == 0:
        return 'P'
    else:
        return  'I'

def media(valor1, valor2):
    try:
        return (valor1+valor1)/2
    except ZeroDivisionError:
        return -1