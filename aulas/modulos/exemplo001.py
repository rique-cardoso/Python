import exp001_uteis as uteis
# import ex001_uteis
# from ex001_uteis import fatorial, dobro, triplo ===> Não recomendado pelo Python, para evitar conflitos.
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')
print(f'O triplo de {num} é {uteis.triplo(num)}.')