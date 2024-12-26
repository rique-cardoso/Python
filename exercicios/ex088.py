import random
numeros = []
jogos = []
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, qtd_jogos):
    for i in range(0, 6):
        while True:
            num = random.randint(1, 60)
            if num in numeros:
                continue
            else:
                numeros.append(num)
                break
    jogos.append(numeros[:])
    numeros.clear()
cont = 1
for jogo in jogos:
    print(f'Jogo {cont}: {jogo}')
    cont += 1