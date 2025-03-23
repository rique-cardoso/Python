class Dog:
    def __init__(self, raca):
        self.idade = 10
        self.raca = raca
    
    def envelhecer(self):
        self.idade += 1

dog = Dog("Lab")
dog2 = Dog("Rsk")

print(dog.idade)
print(dog2.idade)

dog.idade = 13

print(dog.idade)
print(dog2.idade)

print(dog.raca)
print(dog2.raca)

dog.envelhecer()

print(dog.idade)