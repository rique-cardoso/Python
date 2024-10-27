from math import trunc
num = float(input('Digite um número decimal: '))
parte_inteira = trunc(num)
print('A parte inteira do número {} é {}'.format(num, parte_inteira))