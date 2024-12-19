""" num = (2, 5, 9, 1) # Tupla
# num[2] = 3 -> gera erro
print(num) """

num = [2, 5, 9, 1] # Lista
num[2] = 3
# num[4] = 7 -> gera erro, não posso adicionar novos valores desta maneira
num.append(7) # adiciona valor ao final da lista
num.sort() # Ordena crescentemente
num.sort(reverse=True) # Ordena decrescentemente
num.insert(2, 2) # adiciona o valor 2 na posição 2
num.pop() # elimina o último valor
num.pop(2) # elimina o elemento na posição 2
num.remove(2) # elimina a primeira ocorrência do valor 2
# Removendo com cuidado
if 4 in num:
    num.remove(4)
else:
    print('Não há número 4')
print(num)
print(f'essa lista tem {len(num)} valores')