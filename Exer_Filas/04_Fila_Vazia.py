fila = []

for i in range(3):
    nome = input("Digite o nome: ")
    fila.append(nome)

print("\nFila:", fila)

while len(fila) > 0:
    pessoa = fila.pop(0)
    print("Atendendo:", pessoa)

if len(fila) == 0:
    print("A fila esta vazia!")