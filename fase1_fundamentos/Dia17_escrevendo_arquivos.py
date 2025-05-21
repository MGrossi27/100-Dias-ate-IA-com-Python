
# Dia 17 - Escrevendo em Arquivos

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

arquivo = open("usuarios.txt", "w")
arquivo.write(f"Nome: {nome}\nIdade: {idade}\n")
arquivo.close()
print("Dados salvos com sucesso!")
