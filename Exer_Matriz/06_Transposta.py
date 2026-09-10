matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = []

for coluna in range(len(matriz[0])):
    nova_linha = []

    for linha in range(len(matriz)):
        nova_linha.append(matriz[linha][coluna])

    transposta.append(nova_linha)

print("Matriz transposta: ", transposta)
