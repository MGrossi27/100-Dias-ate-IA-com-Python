
# Dia 13 - Funções com Condições

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

n = int(input("Digite um número: "))
print("O número é:", par_ou_impar(n))
