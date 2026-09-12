class Carro:

    total_carros = 0

    def __init__(self, modelo):
        self.modelo = modelo
        Carro.total_carros += 1

carro_1 = Carro("Fusca")
carro_2 = Carro("Gol")
carro_3 = Carro("Civic")

print(f"Total de carros criados: {Carro.total_carros}")