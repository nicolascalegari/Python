notas = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carla": 9.2,
    "Diego": 7.5,
}

soma = 0

for nota in notas.values():

    soma += nota

media = soma / len(notas)

print(f"A média de turma é {media:.2f}")