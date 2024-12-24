numeros = list()
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
        print(n, end=' ')