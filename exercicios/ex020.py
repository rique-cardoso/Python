import random
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))