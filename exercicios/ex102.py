def fatorial(n=1, show=True):
    fat = 1
    if show:
        for i in range(n, 0, -1):
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} =', end='')
            fat *= i
        print(f' {fat}')
    else:
        for i in range(n, 0, -1):
            fat *= i
        print(f'O fatorial de {n} é {fat}.')
n = int(input('Digite um número: '))
res = input('Deseja mostrar o processo de cálculo? [S/N]: ').upper()
show = True if res == 'S' else False
fatorial(n, show)