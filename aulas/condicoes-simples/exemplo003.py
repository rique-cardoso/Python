n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(media))
""" if media >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média, foi ruim. Estude mais!') """
# IF SIMPLIFICADO
print('Parabéns' if media >= 6.0 else 'Estude mais!')