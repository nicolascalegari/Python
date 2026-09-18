from collections import deque

fila_normal = deque()
fila_prioridade = deque()

fila_normal.append("Joao")
fila_normal.append("Maria")

fila_prioridade.append("Carlos")
fila_prioridade.append("Ana")

print("---ATENDIMENTO---")

while fila_prioridade:
    pessoa = fila_prioridade.popleft()
    print("Atendendo prioridade:", pessoa)

while fila_normal:
    pessoa = fila_normal.popleft()
    print("Atendendo normal:", pessoa)

