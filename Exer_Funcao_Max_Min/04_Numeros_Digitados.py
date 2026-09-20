numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")