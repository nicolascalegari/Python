from collections import deque

fila = deque()

for numero in range(1, 6):
    senha = f"{numero:03d}" # Senha de 3 digitos
    fila.append(senha)

print("Senhas geradas:", fila)

while fila:
    senha = fila.popleft()
    print("Chamando senha:", senha)