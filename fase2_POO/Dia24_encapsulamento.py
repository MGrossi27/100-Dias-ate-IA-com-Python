
# Dia 24 - Encapsulamento

class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print("Saldo:", self.__saldo)

c = Conta(500)
c.mostrar_saldo()
