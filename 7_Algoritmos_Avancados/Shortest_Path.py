#Aqui queremos encontrar o menor caminho entre dois pontos em um grafo.
#Podemos usar Dijkstra quando temos pesos positivos.
#Imagine:
#       4
#   A ------- B
#   |         |
# 2 |         | 3
#   |         |
#   C ------- D
#       1
#Queremos ir: A → D
#Temos duas opções:
#A → B → D
#4 + 3 = 7
#ou:
#A → C → D
#2 + 1 = 3
#A resposta é: A → C → D

import heapq

grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 3)],
    "C": [("A", 2), ("D", 1)],
    "D": [("B", 3), ("C", 1)]
}

distancias = {
    "A": 0,
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf")
}

fila = [(0, "A")]

while fila:

    distancia, atual = heapq.heappop(fila)

    if distancia > distancias[atual]:
        continue

    for vizinho, peso in grafo[atual]:

        nova_distancia = distancia + peso

        if nova_distancia < distancias[vizinho]:

            distancias[vizinho] = nova_distancia

            heapq.heappush(
                fila,
                (nova_distancia, vizinho)
            )


print("Menor distância:", distancias["D"])