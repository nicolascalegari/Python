notas = [7,8,9,6]

soma = 0
contador = 0

for nota in notas:
    soma += nota
    contador += 1

media = soma / contador

print("Media: ", media)