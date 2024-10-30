velocidade_carro = float(input('Velocidade em km/h: '))
if velocidade_carro > 80.0:
    diferenca_velocidade = velocidade_carro - 80.0
    valor_multa = 7.0 * diferenca_velocidade
    print('Você foi multado!\nO valor da sua multa é R${:.2f}'.format(valor_multa))