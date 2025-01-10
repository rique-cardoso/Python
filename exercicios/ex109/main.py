import moeda as m
print(f"Aumentando R$10,00 em R$150,00: {m.aumentar(150, 10, True)}")
print(f"Diminuindo R$60,00 em R$160,00: {m.diminuir(160, 60, False)}")
print(f"Dobrando R$100,00: {m.dobro(100, True)}")
print(f"Metade de R$200,00: {m.metade(200, False)}")