#Fatorial e: 5! = 5 × 4 × 3 × 2 × 1

numero = int(input("Digite um numero: "))

resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print(resultado)