import math
import random

numero = random.randint(1, 100)

log_natural = math.log(numero)
log_base10 = math.log10(numero)

print(f"Número sorteado: {numero}")
print(f"Logaritmo natural (ln): {log_natural:.4f}")
print(f"Logaritmo na base 10 (log10): {log_base10:.4f}")