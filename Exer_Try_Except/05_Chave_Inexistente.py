P = {"arroz": 5.20, "feijão": 8.50, "macarrão": 4.00}

try:
    i = input("Digite o nome do produto: ")
    print(f"Preço: R$ {P[i]:.2f}")
except KeyError:
    print("Erro! Produto não encontrado.")