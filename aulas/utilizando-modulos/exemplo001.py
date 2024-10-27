# import math
from math import sqrt, ceil
num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
raiz = sqrt(num)
#print('A raíz quadrada de {} é {:.2f}'.format(num, math.ceil(raiz)))
print('A raíz quadrada de {} é {:.2f}'.format(num, ceil(raiz)))