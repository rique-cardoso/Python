valor_produto = float(input('Preço: '))
desconto = (valor_produto * 5) / 100
valor_final = valor_produto - desconto
print('Total: R${:.2f}\nDescontos: R${:.2f}\nTotal a pagar: R${:.2f}'.format(valor_produto, desconto, valor_final))