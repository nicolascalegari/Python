alunos = {
    "Ana": {"idade": 20, "nota": 8.5},
    "Bruno": {"idade": 22, "nota": 6.0},
    "Carla": {"idade": 19, "nota": 9.2}
}

for nome, dados in alunos.items():

    print(f"{nome} - Idade: {dados['idade']}, Nota: {dados['nota']}")