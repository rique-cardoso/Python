ano = int(input('Ano: '))
teste1 = ano % 4 == 0
teste2 = ano % 100 == 0
teste3 = ano % 400 == 0
if (teste1 and teste2 and teste3) or (teste1 and not teste2):
    print('Este ano é bissexto')
else:
    print('Este não é um ano bissexto')

# CORREÇÃO:

""" ano = int(input('Ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano)) """