#A DFS tenta ir o mais fundo possível antes de voltar.

grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

visitados = set()

def dfs(atual):

    if atual in visitados:
        return

    visitados.add(atual)

    print(atual)

    for vizinho in grafo[atual]:
        dfs(vizinho)

dfs("A")