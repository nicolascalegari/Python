class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self. direita = None

raiz = Node(10)

raiz.esquerda = Node(5)
raiz.direita = Node(20)

raiz.esquerda.esquerda = Node(3)
raiz.esquerda.direita = Node(3)

raiz.direita.esquerda = Node(15)
raiz.direita.direita = Node(30)

#             10
#           /    \
#          5      20
#         / \    /  \
#        3   7  15  30