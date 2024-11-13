idade = int(input('Idade: '))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade > 19 and idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')