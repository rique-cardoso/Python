cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
if valor1 > valor2:
    print('O {}primeiro valor{} é {}maior{}.'.format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa']))
elif valor2 > valor1:
    print('O {}segundo valor{} é {}maior{}.'.format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa']))
else:
    print('{}Não existe{} valor maior, os dois são {}iguais{}.'.format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa']))