class Circle:
    def __init__(self, raio=1):
        self.raio = raio
    
    def calcula_area(self):
        return self.raio * self.raio * 3.14
    
    def retorna_riao(self):
        return self.raio

c1 = Circle()
c2 = Circle(2)

print(c1.raio)
print(c2.raio)

print(c1.calcula_area())
print(c2.calcula_area())

c1.retorna_riao()
c2.retorna_riao()