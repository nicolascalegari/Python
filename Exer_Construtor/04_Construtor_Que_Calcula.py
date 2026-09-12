class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.area = largura * altura

retangulo_1 = Retangulo(5, 3)

print(f"Area: {retangulo_1.area}")