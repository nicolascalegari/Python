a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

print(f"Maior: {maior}")