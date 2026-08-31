#Podemos guardar os resultados já calculados:

memoria = {}

def fibonacci(n):

    if n <= 1:
        return n

    if n in memoria:

        return memoria[n]

    memoria[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memoria[n]

print(fibonacci(40))

#Complexidade O(n).