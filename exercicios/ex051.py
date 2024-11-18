primeiro_termo = int(input('Digite o 1° Termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
for c in range(1, 11):
    termo = primeiro_termo + ((c - 1) * razao)
    print('{}° termo é {}'.format(c, termo))