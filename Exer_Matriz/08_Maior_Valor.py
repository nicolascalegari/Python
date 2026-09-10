matriz = [
    [4, 17, 9],
    [23, 2, 8],
    [11, 6, 30]
]

maior = matriz[0][0]

for linha in matriz:

    for elemento in linha:

        if elemento > maior:

            maior = elemento

print("Maior valor da matriz: ", maior)