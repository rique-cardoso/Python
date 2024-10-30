salario = float(input('Seu salário R$'))
if salario > 1250.00:
    novo_salario = salario + (salario * (10 / 100))
else:
    novo_salario = salario + (salario * (15 / 100))
print('O seu novo salario é R${:.2f}'.format(novo_salario))