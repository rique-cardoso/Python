n = int(input('Digite um número: '))
divisores = 0
if n > 1:
    for c in range(1, n+1):
        if n % c == 0:
            divisores += 1
    
    if divisores == 2:
        print('O número {} é primo porque só tem dois divisores a saber: 1 e {}'.format(n, n))
    else:
        print('O número {} não é um número primo, pois tem mais de dois divisores.'.format(n, n))
else:
    print('O número {} não é um número primo e nem um número composto, é um caso especial.'.format(n))