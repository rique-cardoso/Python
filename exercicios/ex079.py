lista = []
while True:
    element = int(input('Insira um número: '))
    if element not in lista:
        lista.append(element)
    parada = input('Deseja parar? [S/N]').upper()
    if parada == "S":
        break
lista.sort()
print(lista)