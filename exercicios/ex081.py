lista = list()
while True:
    element = int(input('Digite um valor: '))
    lista.append(element)
    parada = input('Deseja parar? ').upper()
    if parada == 'S':
        break
print('='*30)
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente é: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}')
else:
    print('O valor 5 não foi digitado na lista')