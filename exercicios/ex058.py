import random
num = random.randint(1, 5)
num_usuario = 0
while num_usuario != num:
    num_usuario = int(input('Em que número estou pensando? '))
    print('Acertou!' if num == num_usuario else 'Errou!')