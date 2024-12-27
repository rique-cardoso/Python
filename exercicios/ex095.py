jogador = {}
jogadores = []
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['gols'] = list()
    total_jogos = int(input('Quantidade de jogos: '))
    for i in range(0, total_jogos):
        jogador['gols'].append(int(input(f'Quantidade de gols marcados por {jogador["nome"]} na partida {i+1}: ')))
    jogador['total de gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    resposta = input('Deseja continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
print('='*40)
print('cod nome           gols           total')
print('-'*40)
for index, jogador in enumerate(jogadores):
    print(f" {index} {jogador['nome']:<15} {str(jogador['gols']):<15} {jogador['total de gols']:<5}")
