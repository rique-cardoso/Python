jogador = {}
jogadores = []
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['gols'] = list()
    total_jogos = int(input('Quantidade de jogos: '))
    for i in range(0, total_jogos):
        jogador['gols'].append(int(input(f'   Quantidade de gols marcados por {jogador["nome"]} na partida {i+1}: ')))
    jogador['total de gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        resposta = input('Deseja continuar? [S/N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('='*40)
print('cod nome           gols           total')
print('-'*40)
for index, jogador in enumerate(jogadores):
    print(f" {index} {jogador['nome']:<15} {str(jogador['gols']):<15} {jogador['total de gols']:<5}")
print('-'*40)
while True:
    id_jogador = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if id_jogador == 999:
        break
    if id_jogador < 0 or id_jogador >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {id_jogador}!')
    else:
        for index, jogador in enumerate(jogadores):
            if index == id_jogador:
                print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}')
                for indice, gol in enumerate(jogador['gols']):
                    print(f'   No jogo {indice+1} fez {gol} gols.')
                print('-'*40)
print('<< VOLTE SEMPRE >>')