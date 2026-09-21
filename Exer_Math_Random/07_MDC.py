import math
import random

num_1 = random.randint(10, 100)
num_2 = random.randint(10, 100)

# Maximo Divisor Comum
mdc = math.gcd(num_1, num_2)

print(f"Números sorteados: {num_1} e {num_2}")
print(f"O MDC entre {num_1} e {num_2} é: {mdc}")