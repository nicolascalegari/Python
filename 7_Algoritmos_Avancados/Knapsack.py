#Imagine uma mochila com capacidade limitada.
#| Item | Peso | Valor |
#| ---- | ---: | ----: |
#| A    |    2 |     3 |
#| B    |    3 |     4 |
#| C    |    4 |     5 |
#| D    |    5 |     8 |
#A mochila suporta: 5kg
#Queremos obter o maior valor possível.

pesos = [2,3,4,5]
valores = [3,4,5,8]

capacidade = 5

dp = [0] * (capacidade + 1)

for i in range(len(pesos)):
    peso = pesos[i]
    valor = valores[i]
    for capacidade_atual in range(capacidade, peso - 1, -1):
        dp[capacidade_atual] = max(dp[capacidade_atual], dp[capacidade_atual - peso] + valor)

print("Maior valor:", dp[capacidade])