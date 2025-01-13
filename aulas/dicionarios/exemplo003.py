""" estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado)
print(brasil) """

# O código acima é problemática, pois é criado uma relação e não uma cópia, mas também não dá para fazer o fatiamento para criar uma cópia do elemento, para corrigir o problema:

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) # o método copy resolve o problema do fatiamento
print(brasil)

for estado in brasil:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')
for estado in brasil:
    for value in estado.values():
        print(value, end=' ')
    print()