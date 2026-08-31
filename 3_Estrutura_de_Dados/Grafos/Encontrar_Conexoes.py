grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

origem = "A"

for destino in grafo[origem]:
    print("A esta conectado com: ", destino)