#Cada número é a soma dos dois anteriores:
#F(n) = F(n-1) + F(n-2)
#Os casos base são:
#F(0) = 0
#F(1) = 1

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

#Complexidade O(2ⁿ) aproximadamente.