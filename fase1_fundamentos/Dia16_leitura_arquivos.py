
# Dia 16 - Leitura de Arquivos

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print("Conteúdo do arquivo:")
print(conteudo)
arquivo.close()
