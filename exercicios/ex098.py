from time import sleep
def lin():
    print('='*30)
def contador(inicio, fim, passo=1):
    lin()
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    elif inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:
        print(inicio, end='')
    print()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)