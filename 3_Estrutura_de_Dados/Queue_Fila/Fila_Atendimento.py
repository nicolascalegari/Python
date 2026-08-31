from collections import deque

fila = deque(["Cliente 1", "Cliente 2", "Cliente 3"])

while fila:
    cliente = fila.popleft()
    print("Atendendo: ", cliente)