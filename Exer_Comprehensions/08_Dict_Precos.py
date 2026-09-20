produtos = {
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Headset": 200
}

produtos_caros = {
    produto: preco
    for produto, preco in produtos.items()
    if preco > 100
}

print(produtos_caros)