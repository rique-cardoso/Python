matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(num)
for linha in matriz:
    for valor in linha:
        print(f'[  {valor:^5}  ]', end=' ')
    print()
soma_pares = soma_coluna3 = soma_linha2 = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_coluna3 += matriz[i][j]
        if i == 1:
            soma_linha2 += matriz[i][j]
print(f'A soma de todos os valores pares digitados é {soma_pares}')
print(f'A soma de todos os valores da terceira coluna é {soma_coluna3}')
print(f'A soma de todos os valores segunda linha é  {soma_linha2}')