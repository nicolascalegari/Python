notas = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carla": 9.2,
    "Diego": 7.5,
}

melhor_aluno = None
maior_nota = -1

for aluno, nota in notas.items():

    if nota > maior_nota:
        maior_nota = nota
        melhor_aluno = aluno

print(f"O melhor aluno é {melhor_aluno}, com nota {maior_nota}")