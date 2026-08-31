#BFS é especialmente interessante quando todas as conexões possuem o mesmo custo.
#A → B → D
# \       ↑
#  → C → ─
#Queremos descobrir a menor quantidade de conexões entre A e D.

from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

fila = deque([("A", 0)])
visitados = set()

while fila:

    atual, distancia = fila.popleft()

    if atual == "D":
        print("Menor distancia:", distancia)
        break

    if atual in visitados:
        continue

    visitados.add(atual)

    for vizinho in grafo[atual]:
        fila.append((vizinho, distancia + 1))
