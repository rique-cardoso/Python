num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'o número 9 aparece {num.count(9)} vezes')
print(f'O número 3 aparece pela primeira vez no índice {num.index(3)}')
print(f'Os números pares são', end=' ')
for i in num:
    if i % 2 == 0:
        print(f'{i}', end=' ')