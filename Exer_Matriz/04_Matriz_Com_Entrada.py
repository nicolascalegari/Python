linhas = 2
colunas = 2
matriz = []

for i in range(linhas):

    linha_atual = []

    for j in range(colunas):

        valor = int(input(f"Digite o valor para a posicao:[{i}][{j}]: "))
        linha_atual.append(valor)
    matriz.append(linha_atual)

print("Matriz criada: ", matriz)