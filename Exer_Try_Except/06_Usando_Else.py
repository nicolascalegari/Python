try:
    num = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro! Digite um número inteiro.")
else:
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")
