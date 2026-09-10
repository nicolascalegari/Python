matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

resultado = []

for i in range(len(matriz_a)):

    linha_resultado = []

    for j in range(len(matriz_a[i])):

        linha_resultado.append(matriz_a[i][j] + matriz_b[i][j])
    resultado.append(linha_resultado)

print("Soma das matrizes: ", resultado)
