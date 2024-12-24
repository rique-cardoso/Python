lista = []
for i in range(0, 5):
    element = int(input('Insira um valor: '))
    lista.append(element)
print(f'O maior valor digitado foi o valor {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi o valor {min(lista)} na posição {lista.index(min(lista))}')