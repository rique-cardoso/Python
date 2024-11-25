par = impar = 0
c = 1
while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))