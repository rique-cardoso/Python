""" numeros = list()
pares = list()
impares = list()
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
for num in numeros:
    for n in num:
        print(n, end=' ') """

# CORREÇÃO

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}°. Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 60)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')