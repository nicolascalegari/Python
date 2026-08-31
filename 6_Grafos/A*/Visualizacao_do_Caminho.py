#Agora podemos fazer algo um pouco mais completo: encontrar e mostrar o caminho.

import heapq

grid = [
    ["S", ".", ".", "."],
    [".", "#", "#", "."],
    [".", ".", ".", "."],
    [".", "#", ".", "E"]
]

inicio = (0, 0)
fim = (3, 3)


def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


fila = [(0, inicio)]

custos = {inicio: 0}
pais = {inicio: None}

while fila:

    _, atual = heapq.heappop(fila)

    if atual == fim:
        break

    linha, coluna = atual

    for dl, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        vizinho = (linha + dl, coluna + dc)

        l, c = vizinho

        if not (0 <= l < len(grid)):
            continue

        if not (0 <= c < len(grid[0])):
            continue

        if grid[l][c] == "#":
            continue

        novo_custo = custos[atual] + 1

        if vizinho not in custos or novo_custo < custos[vizinho]:

            custos[vizinho] = novo_custo
            pais[vizinho] = atual

            prioridade = (
                novo_custo
                + heuristica(vizinho, fim)
            )

            heapq.heappush(
                fila,
                (prioridade, vizinho)
            )


# Reconstruindo o caminho
caminho = []

atual = fim

while atual is not None:
    caminho.append(atual)
    atual = pais[atual]

caminho.reverse()

print("Caminho:")
print(caminho)
