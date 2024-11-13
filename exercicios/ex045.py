# PEDRA, PAPEL, TESOURA...
import random
import time
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m'}
print('''
-------------------------
   Escolha uma opção: 
-------------------------
    1 - {}PEDRA{}
    2 - {}PAPEL{}
    3 - {}TESOURA{}
__________________________
'''.format(cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa']))
jogada_user = int(input('Opção Escolhida: '))
""" jogada_pc = random.randint(1,3)
print(jogada_pc) """
jogada_pc = 0
jogada_pc = random.randint(1,3)
if jogada_user == 1:
    print('USUÁRIO:')
    time.sleep(2)
    print('... {}PEDRA!{}'.format(cores['amarelo'], cores['limpa']))
    if jogada_pc == 1:
        print('CPU:')
        time.sleep(2)
        print('... {}PEDRA!{}'.format(cores['amarelo'], cores['limpa']))
        time.sleep(3)
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))
    elif jogada_pc == 2:
        print('CPU:')
        time.sleep(2)
        print('... {}PAPEL!{}'.format(cores['vermelho'], cores['limpa']))
        time.sleep(3)
        print('{}DERROTA{}'.format(cores['vermelho'], cores['limpa']))
    elif jogada_pc == 3:
        print('CPU:')
        time.sleep(2)
        print('... {}TESOURA!{}'.format(cores['verde'], cores['limpa']))
        time.sleep(3)
        print('{}VITÓRIA{}'.format(cores['verde'], cores['limpa']))
elif jogada_user == 2:
    print('USUÁRIO:')
    time.sleep(2)
    print('... {}PAPEL!{}'.format(cores['vermelho'], cores['limpa']))
    if jogada_pc == 1:
        print('CPU:')
        time.sleep(2)
        print('... {}PEDRA!{}'.format(cores['amarelo'], cores['limpa']))
        time.sleep(3)
        print('{}VITÓRIA{}'.format(cores['verde'], cores['limpa']))
    elif jogada_pc == 2:
        print('CPU:')
        time.sleep(2)
        print('... {}PAPEL!{}'.format(cores['vermelho'], cores['limpa']))
        time.sleep(3)
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))
    elif jogada_pc == 3:
        print('CPU:')
        time.sleep(2)
        print('... {}TESOURA!{}'.format(cores['verde'], cores['limpa']))
        time.sleep(3)
        print('{}DERROTA{}'.format(cores['vermelho'], cores['limpa']))
elif jogada_user == 3:
    print('USUÁRIO:')
    time.sleep(2)
    print('... {}TESOURA!{}'.format(cores['verde'], cores['limpa']))
    if jogada_pc == 1:
        print('CPU:')
        time.sleep(2)
        print('... {}PEDRA!{}'.format(cores['amarelo'], cores['limpa']))
        time.sleep(3)
        print('{}DERROTA{}'.format(cores['vermelho'], cores['limpa']))
    elif jogada_pc == 2:
        print('CPU:')
        time.sleep(2)
        print('... {}PAPEL!{}'.format(cores['vermelho'], cores['limpa']))
        time.sleep(3)
        print('{}VITÓRIA{}'.format(cores['verde'], cores['limpa']))
    elif jogada_pc == 3:
        print('CPU:')
        time.sleep(2)
        print('... {}TESOURA!{}'.format(cores['verde'], cores['limpa']))
        time.sleep(3)
        print('{}EMPATE{}'.format(cores['amarelo'], cores['limpa']))