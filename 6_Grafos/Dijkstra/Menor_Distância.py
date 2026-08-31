#O objetivo do Dijkstra é encontrar o menor custo de um ponto até os outros.

import heapq

grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 3)],
    "C": [("D", 1)],
    "D": []
}

distancias = {
    "A": 0,
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf")
}

fila = [(0, "A")]

while fila:

    distancia_atual, atual = heapq.heappop(fila)

    for vizinho, peso in grafo[atual]:

        nova_distancia = distancia_atual + peso

        if nova_distancia < distancias[vizinho]:

            distancias[vizinho] = nova_distancia

            heapq.heappush(fila,(nova_distancia, vizinho))

print(distancias)