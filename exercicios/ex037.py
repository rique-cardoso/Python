cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
valor_base10 = int(input('Digite um valor: '))
print('''
-------------------------
   Escolha uma opção: 
-------------------------
    - {}1 para binário{}
    - {}2 para octal{}
    - {}3 para hexadecimal{}
__________________________
'''.format(cores['azul'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa']))
base_conversao = int(input('Opção Escolhida: '))
if base_conversao == 1:
    print("O valor convertido para {}binário{} é {}{}{}.".format(cores['azul'], cores['limpa'], cores['azul'], bin(valor_base10)[2:], cores['limpa']))
elif base_conversao == 2:
    print("O valor convertido para {}octal{} é {}{}{}.".format(cores['vermelho'], cores['limpa'], cores['vermelho'], oct(valor_base10)[2:], cores['limpa']))
elif base_conversao == 3:
    print("O valor convertido para {}hexadecimal{} é {}{}{}.".format(cores['verde'], cores['limpa'], cores['verde'], hex(valor_base10)[2:], cores['limpa']))