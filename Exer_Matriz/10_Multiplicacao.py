matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = int(input("Digite um numero para multiplicar a matriz: "))

resultado = []

for linha in matriz:

    nova_linha = []

    for elemento in linha:

        nova_linha.append(elemento * escalar)

    resultado.append(nova_linha)

print("Matrzi resultante: ", resultado)