numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(numero)

print(f"Soma total da lista: {sum(numeros)}")