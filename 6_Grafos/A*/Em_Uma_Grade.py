#O A* é parecido com Dijkstra, mas possui uma informação adicional chamada heurística.
#A ideia é:
#Não olhar apenas para o custo que já percorremos; também estimar quanto falta até o destino.
#A fórmula principal é: f(n) = g(n) + h(n)
#Onde:
#g(n) = custo desde o início até n
#h(n) = estimativa de n até o destino
#f(n) = prioridade do nó

import heapq

grid = [
    ["S", ".", ".", "#"],
    [".", "#", ".", "."],
    [".", ".", ".", "E"]
]

inicio = (0, 0)
fim = (2, 3)


def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


fila = [(0, inicio)]
custos = {inicio: 0}

while fila:

    _, atual = heapq.heappop(fila)

    if atual == fim:
        print("Destino encontrado!")
        break

    linha, coluna = atual

    vizinhos = [
        (linha + 1, coluna),
        (linha - 1, coluna),
        (linha, coluna + 1),
        (linha, coluna - 1)
    ]

    for vizinho in vizinhos:

        l, c = vizinho

        if l < 0 or l >= len(grid):
            continue

        if c < 0 or c >= len(grid[0]):
            continue

        if grid[l][c] == "#":
            continue

        novo_custo = custos[atual] + 1

        if vizinho not in custos or novo_custo < custos[vizinho]:

            custos[vizinho] = novo_custo

            prioridade = (
                novo_custo
                + heuristica(vizinho, fim)
            )

            heapq.heappush(
                fila,
                (prioridade, vizinho)
            )

#A* considera:
#quanto já percorri + quanto acho que falta