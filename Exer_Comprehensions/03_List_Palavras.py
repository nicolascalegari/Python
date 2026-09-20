nomes = ["joao", "maria", "pedro", "ana"]

nomes_caps = [nome.capitalize() for nome in nomes]

print(nomes_caps)

nomes_a = [nome for nome in nomes if nome.startswith("a")]

print(nomes_a)
