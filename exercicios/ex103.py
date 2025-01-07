def ficha(nome="<desconhecido>", gol=0):
    print(f'O jogador {nome} fez {gol} gols.')
nome = input('Nome do jogador: ').strip()
gol = input('Gols: ')
if gol.isnumeric():
    gol = int(gol)
if nome == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)