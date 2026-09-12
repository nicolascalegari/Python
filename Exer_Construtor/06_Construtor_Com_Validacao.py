class ContaBancaria:

    def __init__(self, titular, saldo):
        if saldo < 0:
            raise ValueError("O saldo inicial não pode se negativo.")
        self.titular = titular
        self.saldo = saldo

conta_1 = ContaBancaria("Carla", 100.00)
print(conta_1.titular, conta_1.saldo)

try:
    conta_2 = ContaBancaria("Diego", -50.00)
except ValueError as erro:
    print("Erro:", erro)