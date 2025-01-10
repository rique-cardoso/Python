import moeda as m
a = m.aumentar(150, 10)
b = m.diminuir(160, 60)
c = m.dobro(100)
d = m.metade(200)
print(f"Aumentando R$10,00 em R$150,00: {m.moeda(a)}")
print(f"Diminuindo R$60,00 em R$160,00: {m.moeda(b)}")
print(f"Dobrando R$100,00: {m.moeda(c)}")
print(f"Metade de R$200,00: {m.moeda(d)}")