codigos = {
    1: "vermelho",
    2: "verde",
    3: "azul"
}

invertido = {}

for chave, valor in codigos.items():

    invertido[valor] = chave

print(invertido)