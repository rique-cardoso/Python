from random import randint
from time import sleep
def sorteia():
    lista = []
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        valor = randint(0, 100)
        lista.append(valor)
        print(valor, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    somaPares(lista)
def somaPares(lista):
    print(f'Somando os valores pares de: {lista}, ', end='', flush=True)
    soma = 0
    for elem in lista:
        if elem % 2 == 0:
            soma += elem
    sleep(1.5)
    print(f'temos {soma}')
sorteia()