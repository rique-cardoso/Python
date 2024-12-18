import random
numAleatorios = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
maior = menor = 0
for indice, elemento in enumerate(numAleatorios):
    if indice == 0:
        maior = elemento
        menor = elemento
    else:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento
print(f'Os valores sorteados foram: {numAleatorios}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')