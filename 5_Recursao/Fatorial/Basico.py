#5! = 5 × 4 × 3 × 2 × 1
#5! = 120
#Matematicamente:
#n! = n × (n - 1)!
#E temos o caso base:
#0! = 1

def fatorial(n):

    if n == 0:
        return 1

    return n * fatorial(n - 1)

print(fatorial(5))

#Complexidade O(n)