precos = {
    "feijão": 8.50,
    "arroz": 5.20,
    "macarrão": 4.00,
}

produto = "arroz"

if produto in precos:

    print(f"O preço de {produto} é R$ {precos[produto]:.2f}")

else:

    print(f"{produto} não encontrado.")