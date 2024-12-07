def converter_para_segundos(tempo):
    h, m, s = map(int, tempo.split(':'))
    return h * 3600 + m * 60 + s

N, M = map(int, input().split())
tempos_ideais = input().split()

tempos_ideais_segundos = [converter_para_segundos(t) for t in tempos_ideais]

penalidades = []

for i in range(M):
    tempos_equipes = list(map(int, input().split()))
    penalidade_total = 0

    for j in range(N):
        tempo_ideal = tempos_ideais_segundos[j]
        tempo_equipe = tempos_equipes[j]

        if tempo_equipe < tempo_ideal:
            penalidade_total += (tempo_ideal - tempo_equipe) * 2
        elif tempo_equipe > tempo_ideal:
            penalidade_total += (tempo_equipe - tempo_ideal) * 1

    penalidades.append(penalidade_total)

menor_penalidade = min(penalidades)
indice_vencedor = penalidades.index(menor_penalidade) + 1

print(f"Equipe vencedora: {indice_vencedor}")
print(f"Penalidade: {menor_penalidade} ponto(s)")
