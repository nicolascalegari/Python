import math

try:
    num = float(input("Digite um número: "))
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz:.2f}")
except ValueError:
    print("Erro: Digite um número valido.")
finally:
    print("Processo finalizado.")