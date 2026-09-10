matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

contador = 0

for linha in matriz:

    for elemento in linha:

        if elemento % 2 == 0:

            contador += 1

print(f"A matriz tem {contador} numeros pares.")