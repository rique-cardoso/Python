lista = []
pares = []
impares = []
while True:
    elem = int(input('Digite um valor: '))
    lista.append(elem)
    parada = input('Deseja parar? [S/N] ').upper()
    if parada == 'S':
        break

for elem in lista:
    if elem % 2 == 0:
        pares.append(elem)
    else:
        impares.append(elem)
print('='*30)
print(f'Valores digitados: {lista}')
print(f'Valores pares digitados: {pares}')
print(f'Valores ímpares digitados: {impares}')