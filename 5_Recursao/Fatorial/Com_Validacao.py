def fatorial(n):

    if n < 0:
        return "Numero invalido"

    if n == 0:
        return 1

    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(-2))

#Complexidade O(n)