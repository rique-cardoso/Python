# ESCOPO DE VARIÁVEIS - resolvendo o problema da repetição de nome de variável em um novo escopo
def teste(b):
    global a # ===> a partir de agora, a será tratado como o 'a' de escopo global
    a = 8
    b += 4 # escopo de bloco
    c = 2 # escopo de bloco
    print(f'FT - "A" dentro vale {a}')
    print(f'FT - "B" dentro vale {b}')
    print(f'FT - "C" dentro vale {c}')
a = 5 # escopo global
teste(a)
print(f'PP - "A" fora vale {a}.')
# print(f'PP - "B" fora vale {b}.') ===> gera erro, pois tem escopo local 
# print(f'PP - "C" fora vale {C}.') ===> gera erro, pois tem escopo local