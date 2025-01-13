def soma(a, b):
    soma = a + b
    return soma
# Programa principal
print(f'8 + 19 = {soma(8, 19)}')
print(f'2 + 15 = {soma(2, 15)}')
print(f'2 + 5 = {soma(2, 5)}')
print(soma(a=4, b=5))
print(soma(b=8, a=10)) # Posso mudar a ordem, desde que eu deixe explícito
# print(soma(a=5, 10)) # Erro -> para explicitar é necessário explicitar todos os parâmetros, se eu explicitar apenas um, vai dar erro
# print(soma(3, 9, 5)) # Erro -> passagem de parâmetros diferente.