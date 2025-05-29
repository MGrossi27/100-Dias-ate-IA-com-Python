
# Dia 25 - Herança

class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au")

c = Cachorro()
c.falar()
