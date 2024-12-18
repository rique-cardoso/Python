tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    if entrada >= 0 and entrada <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {tupla[entrada]}')