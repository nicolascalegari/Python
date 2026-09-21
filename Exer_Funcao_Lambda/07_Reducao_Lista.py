from functools import reduce

numeros = [1, 2, 3, 4]

# Multiplica acumulativamente os elementos da lista
produto = reduce(lambda x, y: x * y, numeros)

print(f"O produto dos elementos é: {produto}")