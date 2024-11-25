primeiro_termo = int(input('Digite o 1° Termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
""" for c in range(1, 11):
    termo = primeiro_termo + ((c - 1) * razao)
    print('{}'.format(termo), end=' → ')
print('FIM') """
c = 0
aux = 1
while c < 10:
    termo = primeiro_termo + ((aux - 1) * razao)
    print('{}'.format(termo), end=' → ')
    c += 1
    aux += 1
    if c == 10:
        maisTermos = int(input('Visualizar mais quantos termos? '))
        if maisTermos != 0:
            c = 10 - maisTermos
        
print('FIM')