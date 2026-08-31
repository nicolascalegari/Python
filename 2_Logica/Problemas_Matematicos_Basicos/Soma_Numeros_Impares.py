numeros = [1,2,3,4,5,6]

soma = 0

for numero in numeros:
    if numero % 2 != 0:
        soma += numero

print(f"Soma dos impares: {soma}")