def dobra(valores):
    for key, valor in enumerate(valores):
        valores[key] = valor*2
    return valores
lista = [1, 2, 3]
listaDobrada = dobra(lista)
print(listaDobrada)