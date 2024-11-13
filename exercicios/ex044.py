cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m'}
valor_produto = float(input('Valor produto: '))
print('''
-------------------------
   Escolha uma opção: 
-------------------------
    - {}1° à vista (dinheiro ou cheque).{}
    - {}2° à vista (cartão){}
    - {}3° 2x no cartão{}
    - {}4° 3x ou mais no cartão{}
__________________________
'''.format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa'], cores['amarelo'], cores['limpa']))
forma_pagametno = int(input('Forma de pagamento: '))
if forma_pagametno == 1:
    print('Valor final do produto: R${:.2f}'.format(valor_produto - ((valor_produto * 10) / 100)))
elif forma_pagametno == 2: 
    print('Valor final do produto: R${:.2f}'.format(valor_produto - ((valor_produto * 5) / 100)))
elif forma_pagametno == 3:
    print('Valor final do produto: R${:.2f}'.format(valor_produto))
elif forma_pagametno == 4:
    print('Valor final do produto: R${:.2f}'.format(valor_produto + ((valor_produto * 20) / 100)))