valor_casa = float(input('Valor do imóvel: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
tempo_parcelamento = int(input('Parcelamento em quantos anos: '))
quantidade_parcelas = tempo_parcelamento * 12
valor_parcela = valor_casa / quantidade_parcelas
valor_maximo_parcela = (salario_comprador * 30) / 100
if valor_parcela > valor_maximo_parcela:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!\nValor da parcela: R${:.2f}'.format(valor_parcela))