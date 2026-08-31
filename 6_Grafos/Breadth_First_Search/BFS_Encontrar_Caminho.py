from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": [] 
}

fila = deque([("A", ["A"])])
visitados = set()

while fila:
    atual, caminho = fila.popleft()

    if atual == "F":
        print("Caminho encontrado:", caminho)
        break

    if atual in visitados:
        continue

    visitados.add(atual)

    for vizinho in grafo[atual]:
        fila.append((vizinho, caminho + [vizinho]))