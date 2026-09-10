numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

grupos = {"pares": [], "impares": []}

for numero in numeros:

    if numero % 2 == 0:

        grupos["pares"].append(numero)

    else:

        grupos["impares"].append(numero)

print(grupos)