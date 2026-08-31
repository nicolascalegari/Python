#Exemplo: 12345 -> 54321

numero = 12345

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print(invertido)