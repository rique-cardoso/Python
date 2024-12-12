""" notas_disponiveis = [
    {"nome": "Cédula de 1 Real", "valor": 1},
    {"nome": "Cédula de 10 Reais", "valor": 10},
    {"nome": "Cédula de 20 Reais", "valor": 20},
    {"nome": "Cédula de 50 Reais", "valor": 50}
]
valor_saque = int(input('Digite o valor que deseja sacar: '))
notas_sacadas = []
aux = valor_saque

while valor_saque > 0:
    for obj in reversed(notas_disponiveis):
        if valor_saque >= obj["valor"]:
            valor_saque -= obj["valor"]
            notas_sacadas.append(obj)
            break
print('Notas sacadas:')
for obj in (notas_sacadas):
    print(obj["nome"]) """

# CORREÇÃO:
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula_atual = 50
total_cedula = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')