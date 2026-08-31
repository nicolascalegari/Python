#O Minimum Spanning Tree (MST) procura conectar todos os vértices de um grafo usando
#Imagine:
#A ----- B
#| \     |
#|  \    |
#C ----- D
#Queremos conectar todas as cidades gastando o mínimo possível.
#Dois algoritmos muito conhecidos são:
#Kruskal
#Prim
#Vamos usar Kruskal

#Temos:
#A -- 4 -- B
#A -- 2 -- C
#B -- 3 -- C
#B -- 5 -- D
#C -- 1 -- D
#Queremos conectar: A, B, C, D gastando o mínimo.

arestas = [
    (1, "C", "D"),
    (2, "A", "C"),
    (3, "B", "C"),
    (4, "A", "B"),
    (5, "B", "D")
]

parent = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D"
}


def encontrar(x):

    if parent[x] != x:
        parent[x] = encontrar(parent[x])

    return parent[x]


def unir(a, b):

    raiz_a = encontrar(a)
    raiz_b = encontrar(b)

    if raiz_a != raiz_b:
        parent[raiz_b] = raiz_a
        return True

    return False


custo_total = 0
arvore = []

for peso, a, b in arestas:

    if unir(a, b):

        arvore.append((a, b, peso))
        custo_total += peso


print("Árvore:", arvore)
print("Custo total:", custo_total)
