from collections import deque

fila = deque()

fila.append("arquivo 1")
fila.append("arquivo 2")
fila.append("arquivo 3")
fila.append("arquivo 4")

while fila:
    documento = fila.popleft()
    print("Imprimindo:", documento)

print("Todos os documentos foram impressos.")