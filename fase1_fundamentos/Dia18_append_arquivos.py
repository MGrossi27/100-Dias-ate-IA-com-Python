
# Dia 18 - Append e with

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome} | Idade: {idade}\n")

print("Dados adicionados com sucesso!")
