numeros = [1, 2, 3, 4, 5]

# Usando map com lambda
quadrados = list(map(lambda x: x ** 2, numeros))

print(f"Lista original: {numeros}")
print(f"Quadrados: {quadrados}")