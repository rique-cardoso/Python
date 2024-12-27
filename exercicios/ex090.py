aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média do(a) aluno(a) {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
for key, value in aluno.items():
    print(f'{key}: {value}')