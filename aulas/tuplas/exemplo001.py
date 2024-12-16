lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Suco
print(lanche[-1]) # Pudim
print(lanche[1:3]) # Suco, Pizza
print(lanche[1:]) # Suco, Pizza, Pudim
print(lanche[:2]) # Hambúrguer, Suco
# Tuplas são imutáveis:
# lanche[1] = 'Refrigerante' -> Gera erros.
# Apresentando tudo num looping
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
for comida in range(0, len(lanche)):
    print(f'Tenho {lanche[comida]}')
print('Tenho comida para caramba')
for posicao, comida in enumerate(lanche):
    print(f'Tenho muitos {comida} na posição {posicao}')
print('Esse loop acima, o enumerate serve para mostrar o conteúdo e a posição do conteúdo na Tupla.')
# Mostrando tamanho da tupla:
print(len(lanche))
# Mostrando a Tupla em ordem:
print(sorted(lanche)) # altera apenas na forma de apresentação, mas a tupla permanece igual.