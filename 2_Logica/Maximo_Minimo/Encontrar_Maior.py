#Sem usar max()

numeros = [10, 25, 8, 40, 15]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Maior: ", maior)