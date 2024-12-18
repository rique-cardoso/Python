listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*43)
print('LISTAGEM DE PREÇOS')
print('-'*43)
for indice in range(0, len(listagem)):
    if indice % 2 == 0:
        print(f'{listagem[indice]:.<30}', end='')
    else:
        print(f'R${listagem[indice]:>10}')