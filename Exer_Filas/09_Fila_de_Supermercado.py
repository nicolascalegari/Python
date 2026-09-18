from collections import deque

fila = deque()

while True:
    nome = input("Digite o nome do cliente (ou 'fim'): ")

    if nome.lower() == "fim":
        break

    fila.append(nome)

print("\n---ATENDIMENTO---")

while fila:
    cliente = fila.popleft()
    print(f"Atendendo: {cliente}")
    print(f"Pessoas restantes: {len(fila)}")

print("\nTodos os clientes foram atendidos!")