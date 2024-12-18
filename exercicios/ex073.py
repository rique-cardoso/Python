teamsBrasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print(20 * '-=')
cincoPrimeiros = teamsBrasileirao[:5]
quatroUltimos = teamsBrasileirao[-4:]
ordemAlfabetica = sorted(teamsBrasileirao)
print('Lista de times do Brasileirão:')
for indice, time in enumerate(teamsBrasileirao):
    print(f'{indice+1} - {time}')
print(20 * '-=')
print('Cinco primeiros colocados:')
for indice, time in enumerate(cincoPrimeiros):
    print(f'{indice+1} - {time}')
print(20 * '-=')
print('Quatro últimos colocados:')
for indice, time in enumerate(quatroUltimos):
    print(f'{indice+17} - {time}')
print(20 * '-=')
print('Times em ordem alfabética:')
for time in ordemAlfabetica:
    print(time)
print(20 * '-=')