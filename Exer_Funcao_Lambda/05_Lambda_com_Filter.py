numeros = [10, 15, 22, 33, 40, 55]

# Usando Filter para terer apenas > 30
maiores_30 = list(filter(lambda x: x > 30, numeros))

print(f"Números originais: {numeros}")
print(f"Maiores que 30: {maiores_30}")