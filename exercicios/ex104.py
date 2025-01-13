""" def leiaInt(string=''):
    num = input(string)
    if num.isnumeric():
        print(f'Você digitou o número {num}')
        return True
    else:
        print(f'Erro! Digite um número inteiro.')
        return False
while True:
    n = leiaInt('Digite um número: ')
    if n:
        break """
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor
# Programa principal
n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')