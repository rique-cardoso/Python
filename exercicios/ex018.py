import math
angulo = int(input('Ângulo: '))
angulo_radian = math.radians(angulo)
seno = math.sin(angulo_radian)
cosseno = math.cos(angulo_radian)
tangente = math.tan(angulo_radian)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))