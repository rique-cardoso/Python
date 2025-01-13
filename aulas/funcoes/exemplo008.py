# PARÂMETROS OPCIONAIS OU PADRÃO
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'{a} + {b} + {c} = {s}')
somar(10, 20, 30)
somar(10, 20)
somar(10)
somar()