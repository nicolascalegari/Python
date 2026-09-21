import math
import random

numero = random.uniform(1.0, 50.0)

teto = math.ceil(numero)
piso = math.floor(numero)
truncado = math.trunc(numero)

print(f"Número original: {numero:.4f}")
print(f"Arredondamento para cima: {teto}")
print(f"Arredondamento para baixo: {piso}")
print(f"Parte inteira (trunc): {truncado}")