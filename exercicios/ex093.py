""" jogador = {}
jogador['nome'] = input('Nome do jogador: ')
jogador['gols'] = list()
total_jogos = int(input('Quantidade de jogos: '))
for i in range(0, total_jogos):
    jogador['gols'].append(int(input(f'Quantidade de gols marcados por {jogador["nome"]} na partida {i+1}: ')))
jogador['total de gols'] = sum(jogador['gols'])
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')
print('=' * 30)
for indice, valor in enumerate(jogador['gols']):
    print(f'Jogo {indice+1} ==> {jogador['nome']} marcou {valor} gols.') """

# CORREÇÃO
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}?  ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')