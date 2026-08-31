import heapq

grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 3)],
    "C": [("D", 1)],
    "D": []
}

fila = [(0, "A", [])]
visitados = set()

while fila:

    distancia, atual, caminho = heapq.heappop(fila)

    if atual in visitados:
        continue

    visitados.add(atual)

    caminho = caminho + [atual]

    if atual == "D":
        print("Caminho:", caminho)
        print("Custo:", distancia)
        break

    for vizinho, peso in grafo[atual]:

        if vizinho not in visitados:

            heapq.heappush(
                fila,
                (distancia + peso, vizinho, caminho)
            )