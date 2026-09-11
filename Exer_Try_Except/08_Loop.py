while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

print(f"Você digitou {num}")