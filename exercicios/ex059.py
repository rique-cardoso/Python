escolha = 0
while escolha != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digte outro número: '))
    print("""
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair do programa""")
    escolha = int(input(''))
    if escolha == 1:
        print('{} + {} = {}'.format(num1, num2, (num1 + num2)))
    elif escolha == 2:
        print('{} x {} = {}'.format(num1, num2, (num1 * num2)))
    elif escolha == 3:
        if num1 != num2:
            print('O maior número é ', end=' ')
            print(num1 if num1 > num2 else num2)
        else:
            print('São iguais.')
    