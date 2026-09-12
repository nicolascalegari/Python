class Produto:

    def __init__(self, nome, preco=0.0):
        self.nome = nome
        self.preco = preco

produto_1 = Produto("Caderno", 15.90)
produto_2 = Produto("Amostra grátis")

print(produto_1.nome, produto_1.preco)
print(produto_2.nome, produto_2.preco)