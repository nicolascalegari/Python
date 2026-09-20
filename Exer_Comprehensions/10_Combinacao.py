numeros = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

# List Comprehension
pares = [numero for numero in numeros if numero % 2 == 0]

# Set Comprehension
impares = {numero for numero in numeros if numero % 2 != 0}

# Dict Comprehension
dobros = {numero: numero * 2 for numero in numeros}

# Generator Comprehension
quadrados = (numero ** 2 for numero in numeros)

print("Pares:", pares)
print("Impares:", impares)
print("Dobros:", dobros)

print("Quadrados:") 
for numero in quadrados: print(numero)