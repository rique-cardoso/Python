from math import hypot
cateto_a = float(input('Digite o cateto A: '))
cateto_b = float(input('Digite o cateto B: '))
hipotenusa = hypot(cateto_a, cateto_b)
print('A hipotenusa equivalente é {:.2f}'.format(hipotenusa))