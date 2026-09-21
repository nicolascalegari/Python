import math
import random

# Angulo aleatorio
angulo_graus = random.uniform(0, 360)

# Converter para radianos
angulo_radianos = math.radians(angulo_graus)

# Calculo seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Angulo: {angulo_graus:.2f}")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")