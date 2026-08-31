#A Programação Dinâmica (DP) é utilizada quando um problema pode ser dividido em subproblemas que se repetem.
#Resolver uma vez e guardar o resultado para não precisar calcular novamente.

def fibonacci(n):

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(fibonacci(10))

#Tempo: O(n)
#Espaço: O(n)