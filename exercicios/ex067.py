n = 0
while True:
    c = 0
    n = int(input('Digite um número: '))
    if n < 0:
        break
    while c < 11:
        print(f'{n} x {c} = {n * c}')
        c += 1