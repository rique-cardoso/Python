galera = list()
dado = list()
total_maior = total_menor = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor += 1
print(f'Temos {total_maior} pessoas maiores de idade e {total_menor} pessoas menor de idade')