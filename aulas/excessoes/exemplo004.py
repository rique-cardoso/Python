try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    # print('Infelizmente, tivemos um problema :(')
    print(f'Erro encontrador {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print(f'Volte sempre!')