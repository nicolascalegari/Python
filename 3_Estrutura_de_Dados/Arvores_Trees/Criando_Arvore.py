#Uma Tree (Árvore) organiza dados de maneira hierárquica.
#             10
#           /    \
#          5      20
#         / \    /  \
#        3   7  15  30
#Root → raiz (10)
#Children → filhos
#Parent → pai
#Leaf → folha
#Branch → ramificação

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = Node(10)

raiz.esquerda = Node(5)
raiz.direita = Node(20)

print(raiz.valor)
print(raiz.esquerda.valor)
print(raiz.direita.valor)

#       10
#      /  \
#     5    20