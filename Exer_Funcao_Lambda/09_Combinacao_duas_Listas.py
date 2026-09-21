lista_1 = [1, 2, 3]
lista_2 = [10, 20, 30]

soma_listas = list(map(lambda x, y: x + y, lista_1, lista_2))

print(f"Soma elemento a elemento: {soma_listas}")