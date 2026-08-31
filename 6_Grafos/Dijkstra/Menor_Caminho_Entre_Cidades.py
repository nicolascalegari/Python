#São Paulo → Campinas = 100
#São Paulo → Santos = 80
#Campinas → Ribeirão Preto = 220
#Santos → Ribeirão Preto = 400

import heapq

grafo = {
    "Sao Paulo": [
        ("Campinas", 100),
        ("Santos", 80)
    ],

    "Campinas": [
        ("Ribeirao Preto", 220)
    ],

    "Santos": [
        ("Ribeirao Preto", 400)
    ],

    "Ribeirao Preto": []
}

fila = [(0, "Sao Paulo")]
distancias = {
    "Sao Paulo": 0,
    "Campinas": float("inf"),
    "Santos": float("inf"),
    "Ribeirao Preto": float("inf")
}

while fila:

    distancia, cidade = heapq.heappop(fila)

    for vizinho, distancia_aresta in grafo[cidade]:

        nova_distancia = distancia + distancia_aresta

        if nova_distancia < distancias[vizinho]:

            distancias[vizinho] = nova_distancia

            heapq.heappush(
                fila,
                (nova_distancia, vizinho)
            )

print(distancias)