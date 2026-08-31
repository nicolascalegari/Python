#Usando For

nomes = ["Joao", "Maria", "Carlos", "Ana"]

procurado = "Carlos"
encontrado = False

for nome in nomes:
    if nomes == procurado:
        encontrado = True

if encontrado:
    print("Encontrado")
else:
    print("Nao encontrado")