""" numero = input('Digite um número de até 4 casas: ')
tamanho = len(numero)

if tamanho == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
elif tamanho == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    print('Unidade: {}\nDezena: {}\nCentena: {}'.format(unidade, dezena, centena))
elif tamanho == 2:
    unidade = numero[1]
    dezena = numero[0]
    print('Unidade: {}\nDezena: {}'.format(unidade, dezena))
elif tamanho == 1:
    print('Unidade: {}'.format(numero))
else:
    print('ERRO') """

# CORREÇÃO

numero = int(input('Digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))