jogador = {}
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
    print(f'Jogo {indice+1} ==> {jogador['nome']} marcou {valor} gols.')