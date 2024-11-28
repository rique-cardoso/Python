qtd_termos = 0
while qtd_termos <= 0:
    qtd_termos = int(input('Quantos termos você quer mostrar?'))
c = 0
anterior = 0
proximo = 1
aux = 0
print(c, end=' → ')
if qtd_termos > 1:
    print(1, end=' → ')
    while c < (qtd_termos - 2):
        print(anterior + proximo, end=' → ')
        aux = proximo
        proximo = anterior + proximo
        anterior = aux
        c += 1
print('FIM')