import math
import random

secreto = random.randint(1, 3)
palpite = random.randint(1, 3)

# Calcule a diferença absoluta
diferenca = math.fabs(secreto - palpite)

print(f"Número secreto: {secreto}")
print(f"Palpite do robô: {palpite}")
print(f"Diferença absoluta: int({diferenca})")

if secreto == palpite:
    print("O robô acertou em cheio!")
else:
    print("O robô errou.")