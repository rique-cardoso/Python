# ESCOPO DE VARIÁVEIS
def teste():
    x = 8 # ===> variável com escopo local ou escopo de bloco | funciona apenas dentro da função teste()
    print(f'FT - Na função teste(), a variável n vale {n}.')
    print(f'FT - Na função teste(), a variável x vale {x}.')
n = 3 # ===> variável com escopo global | funciona no código todo
print(f'PP - No programa principal, a variável n vale {n}.')
teste()
# print(f'PP - No programa principal, a variável x vale {x}.') ===> gera erros, por conta de escopo de variáveis