#Exercício 1
nomes = []
sexos = []
placas = []
valores = []
km_contratados = []
dias_contratados = []
qtd_clientes = []

while True:
    nome = input('Digite o nome do cliente: ')
    nomes.append(nome)
    sexo = input('Digite o sexo do cliente[M/F]: ')
    sexos.append(sexo)
    placa = input('Digite a placa do carro: ')
    placas.append(placa)
    qtd_km = float(input('Quantos Quilômetros deseja contratar? '))
    km_contratados.append(qtd_km)
    qtd_dias = int(input('Quantos dias deseja conntratar? '))
    dias_contratados.append(qtd_dias)
    qtd_clientes.append(1)
    valor_cobrado = (70 * qtd_dias) + (0.10 * qtd_km)
    valores.append(valor_cobrado)

    sair = input('Se desejar encerrar o programa digite [SAIR]: ')
    if sair == 'SAIR':
        break

for i in range(len(nomes)):
    print(f'O carro de placa {placas[i]} vai pagar {valores[i]}')

for i in range (len(sexos)):
    if sexos[i] == 'F' and dias_contratados[i] > 7:
        print(f'A Cliente {nomes[i]} Alugou o carro por {dias_contratados[i]}')

print(f'A Média de KM Contratados é de: {sum(km_contratados)/len(qtd_clientes)} ')
