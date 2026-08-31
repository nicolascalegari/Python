notas = [7, 8, 9, 6]

for nota in notas:
    print(nota)

#Ou calcular media
notas = [7, 8, 9, 6]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas) #len()Conta o tamanho do array/list

print("Media: ", media)