n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(soma, multiplicacao, divisao), end = '')
print('A divisão inteira é {} e a potência é {}.'.format(divisao_inteira, exponenciacao))