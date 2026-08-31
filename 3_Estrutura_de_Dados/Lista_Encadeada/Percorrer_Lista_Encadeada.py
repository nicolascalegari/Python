class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.proximo = node2
node2.proximo = node3

atual = node1

while atual is not None:
    print(atual.valor)
    atual = atual.proximo