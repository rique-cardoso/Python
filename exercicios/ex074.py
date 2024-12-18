import random
numAleatorios = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(f'Os números sorteados foram: {numAleatorios}')
print(f'O maior número é {max(numAleatorios)}')
print(f'O menor número é {min(numAleatorios)}')