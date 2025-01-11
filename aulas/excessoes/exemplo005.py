try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não inserir dados.')
except Exception as erro:
    print(f'Erro: {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print(f'Volte sempre!')