labirinto = [
    ["S", ".", "#"],
    ["#", ".", "#"],
    ["#", ".", "E"]
]

# S = inicio
# E = saida
# . = caminho
# # = Parede

def encontrar_saida(labirinto, linha, coluna, visitados):

    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # Está fora do labirinto
    if linha < 0 or linha >= linhas:
        return False

    if coluna < 0 or coluna >= colunas:
        return False

    # É uma parede
    if labirinto[linha][coluna] == "#":
        return False

    # Já visitamos
    if (linha, coluna) in visitados:
        return False

    # Encontrou a saída
    if labirinto[linha][coluna] == "E":
        return True

    visitados.add((linha, coluna))

    # Tenta baixo
    if encontrar_saida(labirinto, linha + 1, coluna, visitados):
        return True

    # Tenta direita
    if encontrar_saida(labirinto, linha, coluna + 1, visitados):
        return True

    # Tenta cima
    if encontrar_saida(labirinto, linha - 1, coluna, visitados):
        return True

    # Tenta esquerda
    if encontrar_saida(labirinto, linha, coluna - 1, visitados):
        return True

    return False


visitados = set()

print(encontrar_saida(labirinto, 0, 0, visitados))