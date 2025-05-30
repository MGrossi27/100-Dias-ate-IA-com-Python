
# Dia 26 - Polimorfismo

class Forma:
    def desenhar(self):
        print("Desenhando forma")

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando círculo")

def desenhar_forma(f):
    f.desenhar()

desenhar_forma(Forma())
desenhar_forma(Circulo())
