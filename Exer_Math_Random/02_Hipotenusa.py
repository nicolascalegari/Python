import math
import random

cateto_1 = random.randint(1, 20)
cateto_2 = random.randint(1, 20)

# Calculo da hipotenusa
hipotenusa = math.hypot(cateto_1, cateto_2)

print(f"Cateto 1: {cateto_1}")
print(f"Cateto 2: {cateto_2}")
print(f"A hipotenusa é: {hipotenusa:.2f}")