#A ideia é procurar um caminho entre S e E.

import heapq

mapa = [
    ["S", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", ".", "E"]
]

inicio = (0, 0)
destino = (4, 4)


def heuristica(posicao, destino):
    return (
        abs(posicao[0] - destino[0])
        + abs(posicao[1] - destino[1])
    )


fila = [(0, inicio)]
custos = {inicio: 0}

while fila:

    _, atual = heapq.heappop(fila)

    if atual == destino:
        print("Destino encontrado!")
        break

    linha, coluna = atual

    for dl, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        novo = (linha + dl, coluna + dc)

        l, c = novo

        if not (0 <= l < len(mapa)):
            continue

        if not (0 <= c < len(mapa[0])):
            continue

        if mapa[l][c] == "#":
            continue

        custo = custos[atual] + 1

        if novo not in custos or custo < custos[novo]:

            custos[novo] = custo

            f = custo + heuristica(novo, destino)

            heapq.heappush(fila, (f, novo))

#A heurística ajuda o algoritmo a priorizar posições que parecem estar mais próximas do destino.