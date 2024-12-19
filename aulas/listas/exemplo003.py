a = [2, 3, 4, 7]
b = a
b[2] = 8 # vai colocar 8 nas duas listas, pois quando igualei elas, o Python cria uma ligação entre elas
print(a)
print(b)
# uma forma de evitar este problema de ligação entre as listas é fazer com que b receba uma cópia dos elementos de a, faremos isso abaixo com c e d
c = [4, 6, 8, 14]
d = c[:]
d[2] = 16
print(c)
print(d)