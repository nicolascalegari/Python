sequencia = [5, 8, 12, 3, 9, 15, 1]

for indice, valor in enumerate(sequencia):

    if indice % 3 == 0:

        print(f"Indice {indice} (multiplo de 3): {valor}")

    else:

        print(f"Indice {indice}: {valor}")