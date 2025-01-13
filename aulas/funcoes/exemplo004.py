# Empacotador de parâmetros
# Muito útil para quando eu não sei quantos parâmetros serão passados exatamente
def contador(*num):
    print(type(num), end=' ')
    print(num)
contador(5, 3, 5, 10)
contador(10)
contador(2, 3)

def soma(*num):
    return sum(num)
print(soma(3, 5, 10, 20))
print(soma(3, 5))
print(soma(30, 50))

def soma(*num):
    for indice, elem in enumerate(num):
        if indice != (len(num) - 1):
            print(f'{elem} + ', end='')
        else:
            print(f'{elem}', end='')
    print(f' = {sum(num)}')

soma(10, 15)
soma(10, 10, 10, 10, 10)
soma(10, 10, 30)