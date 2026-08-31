#BFS (Busca em Largura) explora o grafo nível por nível.
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F
#Começando em A, a BFS visita:
#A → B → C → D → E → F
#Ela primeiro visita os vizinhos mais próximos antes de avançar.
#BFS normalmente utiliza uma Queue (fila):

from collections import deque

grafo = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[]
}

fila = deque(["A"])
visitados = set()

while fila:
    atual = fila.popleft()

    if atual in visitados:
        continue

    visitados.add(atual)

    print(atual)

    for vizinho in grafo[atual]:
        fila.append(vizinho)

#Complexidade
#Tempo: O(V + E)
#V = número de vértices
#E = número de arestas