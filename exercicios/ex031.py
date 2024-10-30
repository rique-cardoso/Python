distancia = float(input('Distância em km: '))
if distancia <= 200:
    valor_passagem = 0.5 * distancia
    print('Valor da passagem R${:.2f}'.format(valor_passagem))
else:
    valor_passagem = 0.45 * distancia
    print('Valor da passagem R${:.2f}'.format(valor_passagem))