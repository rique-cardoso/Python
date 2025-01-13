nome = []
medias = []
boletim = []
while True:
    nome.append(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    medias.append(media)
    resposta = input('Deseja continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
boletim.append(nome[:])
boletim.append(medias[:])
print(len(nome))
print(len(medias))
print('='*40)
print('BOLETIM')
print('='*40)
for coluna in range(0, len(nome)):
    print(f'{coluna:^10} | ', end='')
    for linha in range(0, len(boletim)):
        print(f'{boletim[linha][coluna]:^10} | ', end='')
    print()