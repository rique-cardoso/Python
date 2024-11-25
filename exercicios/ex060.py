num = int(input('Digite um número: '))
print('!{} = '.format(num), end=' ')
c = num - 1
resultado = num * c
print(num, end=' ')
while c != 0:
    print('x {}'.format(c), end=' ')
    c -= 1
    if c != 0:
        resultado = resultado * c
print('= {}'.format(resultado))