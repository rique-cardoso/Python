a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # concatena as duas tuplas
c = b + a # a ordem da concatenação altera o resultado
print(c.count(5)) # conta quantas vezes há a ocorreância de um elemento em uma Tupla.
print(c.index(8)) # mostra a posição em que está um determinado elemento, na sua primeira ocorrência
print(c.index(5, 1)) # mostra a posição em que está um determinado elemento, na sua primeira ocorrência, começando a contar a partir de uma posição especificada
# Tuplas aceitam dados de diferentes tipos primitivos
pessoa = ('Gustavo', 39, 'M', 99.88)
# Exclusão de Tuplas:
del(pessoa)
# print(pessoa) -> vai gerar erro, pois ela foi apagada
# não é possível deletar um ítem específico na tupla, apenas a exclusão dela toda
