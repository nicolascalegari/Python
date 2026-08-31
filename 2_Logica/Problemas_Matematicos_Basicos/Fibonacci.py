n = int(input("Informe qtd de sequencia de fibonacci: "))

a = 0
b = 1

for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo