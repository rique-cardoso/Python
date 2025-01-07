def leiaInt(string=''):
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
        break