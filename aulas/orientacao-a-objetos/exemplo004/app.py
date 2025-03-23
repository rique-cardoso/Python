# HERANÇA

class Animal:
    def __init__(self):
        print("Animal criado")

    def quem_sou_eu(self):
        print("Eu sou um animal.")

    def comer(self):
        print("Comendo")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Eu sou um cachorro")

    def quem_sou_eu(self):
        print("Eu sou um cachorro")

animal = Animal()

dog = Cachorro()
