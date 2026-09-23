valor_compra = 150.00

valor_final = valor_compra * 0.9 if valor_compra > 100 else valor_compra

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Valor com desconto (se aplicavel): R$ {valor_final:.2f}")