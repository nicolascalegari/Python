from collections import deque

fila = deque()

fila.append("A") # Enfileirar
fila.append("B") # Enfileirar

fila.popleft() # Desenfileirar

print(fila) # Monstrar fila

len(fila) # Quantidade de elementos

if fila: # Verificar se possui elementos
    print("Não esta vazia")