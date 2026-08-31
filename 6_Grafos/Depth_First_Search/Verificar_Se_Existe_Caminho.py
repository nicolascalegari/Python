#Podemos usar DFS para procurar um determinado vértice.

grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

visitados = set()

def existe_caminho(atual, destino):

    if atual == destino:
        return True

    visitados.add(atual)

    for vizinho in grafo[atual]:

        if vizinho not in visitados:

            if existe_caminho(vizinho, destino):
                return True

    return False


print(existe_caminho("A", "F"))