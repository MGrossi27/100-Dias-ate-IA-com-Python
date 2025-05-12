
# Dia 8 - Break e Continue

numero_secreto = 7

while True:
    palpite = int(input("Adivinhe o número (0-10): "))
    
    if palpite == numero_secreto:
        print("Acertou!")
        break
    else:
        print("Tente novamente...")
