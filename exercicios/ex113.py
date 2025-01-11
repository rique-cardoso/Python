def leiaInt(string=''):
    try:
        num = int(input(string))
    except Exception as e:
        num = e
    finally:
        return num
def leiaFloat(string=''):
    try:
        num = float(input(string))
    except Exception as e:
        num = e
    finally:
        return num
numero = leiaInt("Digite um número: ")
numero2 = leiaFloat("Digite outro número: ")
print(f'Numero 1: {numero}')
print(f'Numero 2: {numero2}')