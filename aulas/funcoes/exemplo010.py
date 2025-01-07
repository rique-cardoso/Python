# ESCOPO DE VARIÁVEIS
def teste(b):
    a = 8 # escopo de bloco ===> NÃO ATUALIZA O VALOR DE "A" -> apenas cria uma nova variável chamada 'a', porém com escopo de bloco
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