aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] > 7.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for key, value in aluno.items():
    print(f'{key}: {value}')