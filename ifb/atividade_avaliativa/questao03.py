def soma(x, y):
    try:
        s = x + y
    except Exception as e:
        return f'Erro: {e}'
    else:
        return s
def subtracao(x, y):
    try:
        s = x - y
    except Exception as e:
        return f'Erro: {e}'
    else:
        return s
def multiplicacao(x, y):
    try:
        m = x * y
    except Exception as e:
        return f'Erro: {e}'
    else:
        return m
def divisao(x, y):
    try:
        d = x / y
    except Exception as e:
        return f'Erro: {e}'
    else:
        return d
def operacoes(x, y):
    a = soma(x,y)
    s  = subtracao(x, y)
    m = multiplicacao(x, y)
    d = divisao(x,y)
    resultado = {
        "soma": a,
        "subtracao": s,
        "multiplicacao": m,
        "divisao": d
    }
    return resultado
x = y = 0
while True:
    try:
        x = float(input('Digite um valor: '))
        y = float(input('Digite outro valor: '))
    except:
        continue
    else:
        break
res = operacoes(x, y)
for key, value in res.items():
    print(f'A {key} de {x} e {y} é igual a {value}')
    print('-'*30)