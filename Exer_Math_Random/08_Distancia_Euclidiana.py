import math
import random

ponto_a = (random.randint(-10, 10), (random.randint(-10, 10)))
ponto_b = (random.randint(-10, 10), (random.randint(-10, 10)))

# Calcula a distancia entre os pontos
distancia = math.dist(ponto_a, ponto_b)

print(f"Ponto A: {ponto_a}")
print(f"Ponto B: {ponto_b}")
print(f"A distância euclidiana é: {distancia:.2f}")