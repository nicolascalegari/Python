class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

#Funcao de busca
def buscar(raiz, valor):
    if raiz is None:
        return False

    if raiz.valor == valor:
        return True

    return (
        buscar(raiz.esquerda, valor)
        or buscar(raiz.direita, valor)
    )

raiz = Node(10)

raiz.esquerda = Node(5)
raiz.direita = Node(20)

raiz.esquerda.esquerda = Node(3)
raiz.esquerda.direita = Node(7)

print(buscar(raiz, 7))
print(buscar(raiz, 100))