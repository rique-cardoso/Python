salario_atual = float(input('Salário atual: '))
aumento = (salario_atual * 15) / 100
novo_salario = salario_atual + aumento
print('Novo salário: R${:.2f}'.format(novo_salario))