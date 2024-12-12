notas_disponiveis = [
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
    print(obj["nome"])