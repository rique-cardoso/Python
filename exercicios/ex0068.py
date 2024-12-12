import random
while True:
    escolha_user = input('Escolha Par ou Ímpar (P, I): ').upper()
    numero_user = int(input('Digite um valor: '))
    jogada_pc = random.randint(1, 100)
    soma = numero_user + jogada_pc
    perdeu = False
    if escolha_user == 'P':
        if soma % 2 == 0:
            print(f'O computador jogou {jogada_pc}. A soma é {soma}.\nParabéns você venceu!')
        else:
            print(f'O computador jogou {jogada_pc}. A soma é {soma}.\nVocê perdeu!')
            perdeu = True
    else:
        if soma % 2 != 0:
            print(f'O computador jogou {jogada_pc}. A soma é {soma}.\nParabéns, você venceu!')
        else:
            print(f'O computador jogou {jogada_pc}. A soma é {soma}.\nVocê perdeu.')
            perdeu = True
    if perdeu == True:
        break