#Podemos fazer a mesma ideia sem recursão.

grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

pilha = ["A"]
visitados = set()

while pilha:

    atual = pilha.pop()

    if atual in visitados:
        continue

    visitados.add(atual)

    print(atual)

    for vizinho in grafo[atual]:
        pilha.append(vizinho)

#É exatamente o comportamento de uma Stack — LIFO.