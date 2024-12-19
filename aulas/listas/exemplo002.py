# Imprimindo na tela uma lista de forma mais bonitinha
valores = list()
valores.append(2)
valores.append(5)
valores.append(8)
for valor in valores:
    print(valor)

for chave, valor in enumerate(valores):
    print(f'Na posição {chave}, econtrei {valor}')

# Entrada de dados dinamicamente

for valor in range(0, 10):
    valores.append(int(input('Digite um valor: ')))

print(valores)