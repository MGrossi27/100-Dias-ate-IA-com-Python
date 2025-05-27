
# Dia 23 - __init__ e Métodos Especiais

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

p = Pessoa("Ana", 30)
print(p)
