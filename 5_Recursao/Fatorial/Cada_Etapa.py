def fatorial(n):

    if n == 0:
        print("Chegou no caso base")
        return 1

    print("Calculando:", n)

    resultado = n * fatorial(n - 1)

    print("Retornando:", resultado)

    return resultado

print("Resultado:", fatorial(5))

#Complexidade O(n)