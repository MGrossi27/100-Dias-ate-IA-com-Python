
# Dia 27 - Classes Abstratas

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("Carro em movimento")

c = Carro()
c.mover()
