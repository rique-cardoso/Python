cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('{}REPROVADO{}'.format(cores['vermelho'], cores['limpa']))
elif media >= 5.0 and media <= 6.9:
    print('{}RECUPERAÇÃO{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}APROVADO{}'.format(cores['verde'], cores['limpa']))