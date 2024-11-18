maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if c == 0:
        menor = peso
    if peso < menor:
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))