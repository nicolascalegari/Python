def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(17, 5)

print(f"Quociente: {q}, Resto: {r}")