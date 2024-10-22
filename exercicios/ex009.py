numero = int(input('Digite um número: '))
ponto_parada = int(input('Digite o número de parada: '))
for i in range(ponto_parada + 1):
    produto = i * numero
    print('{} x {} = {}'.format(i, numero, produto))