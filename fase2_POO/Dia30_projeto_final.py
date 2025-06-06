
# Dia 30 - Projeto Final: Sistema de Cadastro com POO

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, estudante de {self.curso}"

lista = []
while True:
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    lista.append(Estudante(nome, idade, curso))

    cont = input("Deseja adicionar mais? (s/n): ")
    if cont.lower() != 's':
        break

print("\nAlunos cadastrados:")
for estudante in lista:
    print(estudante)
