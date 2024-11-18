maiores = 0
menores = 0
for c in range(0, 7):
    ano_nasc = int(input('Ano de nascimento: '))
    idade = 2024 - ano_nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} já atingiram a maioridade, enquanto que os outros {} ainda são de menor.'.format(maiores, menores))