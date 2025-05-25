
# Dia 20 - Desafio Final da Fase 1

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu e-mail: ")

with open("cadastros.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | Idade: {idade} | Email: {email}\n")

print("\nLista de cadastrados:")
with open("cadastros.txt", "r") as arquivo:
    print(arquivo.read())
