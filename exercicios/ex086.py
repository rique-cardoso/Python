""" matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(num)
for linha in matriz:
    for valor in linha:
        print(f'[  {valor:^5}  ]', end=' ')
    print() """

# CORREÇÃO

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()