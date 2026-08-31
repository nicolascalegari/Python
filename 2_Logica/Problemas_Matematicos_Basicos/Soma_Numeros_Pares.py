numeros = [1,2,3,4,5,6,7,8]

contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print(f"Quantidade de pares: {contador}")