dias = int(input('Quantidade de dias alugado: '))
km = float(input('km rodados: '))
valor_dias = 60 * dias
valor_km = 0.15 * km
valor_total = valor_dias + valor_km
print('O valor total do aluguel é R${:.2f}'.format(valor_total))