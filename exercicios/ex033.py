num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        menor = num3
    else:
        menor = num2
elif num2 > num3:
    maior = num2
    if num1 > num3:
        menor = num3
    else:
        menor = num1
else:
    maior = num3
    if num2 > num1:
        menor = num1
    else:
        menor = num2
print('O maior número é {}\nO menor número é {}'.format(maior, menor))


# CORREÇÃO:
""" a = int(input('Número 1: '))
b = int(input('Número 2: '))
c = int(input('Número 3: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior)) """