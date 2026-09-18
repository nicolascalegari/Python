# Importando deque
# Internamente mais rapido que usar pop(0)
from collections import deque

fila = deque()

fila.append(10)
fila.append(20)
fila.append(30)
fila.append(40)
fila.append(50)

print("Fila:", fila)

print("Removido:", fila.popleft()) #Funcao do deque que foi importado
print("Removido:", fila.popleft()) #Funcao do deque que foi importado

print("Fila restante:", fila)