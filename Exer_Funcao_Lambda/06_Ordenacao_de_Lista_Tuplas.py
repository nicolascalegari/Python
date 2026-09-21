pessoas = [('Ana', 25), ('Carlos', 19), ('Beatriz', 30)]

# Ordenando com base no segundo elemento da tupla (indice 1)
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(f"Pessoas ordenadas por idade: {pessoas_ordenadas}")