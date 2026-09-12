class Animal:

    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):

    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

cachorro_1 = Cachorro("Rex", "Labrador")

print(f"Nome: {cachorro_1.nome}, Raça: {cachorro_1.raca}")