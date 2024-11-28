maior = 0
menor = 0
media = 0
soma = 0
qtd = 0
resposta = 'S'
while resposta != 'N':
    num = int(input('Digite um número: '))
    if qtd == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    qtd += 1
    resposta = input('Quer continuar? [s/n]: ').upper()
print('Você digitou {} números\nA média desses números é {}\nO maior número digitado foi {}\nO menor número digitado foi {}'.format(qtd, (soma / qtd), maior, menor))