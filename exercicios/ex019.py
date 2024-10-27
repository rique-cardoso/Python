import random
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(alunos)
print('O aluno que vai apagar a lousa é {}'.format(aluno_sorteado))