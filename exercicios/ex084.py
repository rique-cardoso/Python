pessoas = list()
dados = list()
maisLeves = list()
maisPesados = list()
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    parada = input('Deseja parar? [S/N] ').upper()
    if parada == 'S':
        break
for pessoa in pessoas:
    if pessoa[1] <= 70.0:
        maisLeves.append(pessoa[0])
    elif pessoa[1] >= 100.0:
        maisPesados.append(pessoa[0])
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são: {maisPesados}')
print(f'As pessoas mais leves são: {maisLeves}')