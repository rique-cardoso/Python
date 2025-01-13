teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste) # Cria-se uma ligação, para isso é necessário fazer uma cópia
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)