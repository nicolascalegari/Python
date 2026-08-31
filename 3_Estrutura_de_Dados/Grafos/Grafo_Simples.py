#Um Graph (Grafo) representa objetos e suas conexões.
#Por exemplo, imagine cidades:
#São Paulo ─── Campinas
#     │            │
#     │            │
#   Santos ─── Ribeirão Preto
#Cada cidade é um vértice (node) e cada ligação é uma aresta (edge).

#Podemos representar um grafo usando um dicionário:

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print(grafo)

#Isso significa:
#A → B
#A → C
#B → A
#B → D
#C → A
#D → B

#Visualmente:
#    A
#   / \
#  B   C
#  |
#  D