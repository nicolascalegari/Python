#1 + 2 + 3 + 4 + 5 = 15

n = int(input("Soma dos N numeros: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print(soma)

#Outra maneira de resolver:

n = int(input("Soma dos N numeros: "))

soma = n * (n + 1) // 2

print(soma)