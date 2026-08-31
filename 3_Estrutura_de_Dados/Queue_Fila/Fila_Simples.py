#Semelhante a uma fila de banco
#O primeiro que entra e o primeiro que sai

from collections import deque

fila = deque()

fila.append("Joao")
fila.append("Maria")
fila.append("Carlos")

print(fila)

primeiro = fila.popleft()

print("Saiu: ", primeiro)

print(fila)
