#Exemplo: MDC(12, 18) = 6

a = 12
b = 18

while b != 0:
    resto = a % b
    a = b
    b = resto

print("MDC: ", a)

#Algoritmo de Euclides