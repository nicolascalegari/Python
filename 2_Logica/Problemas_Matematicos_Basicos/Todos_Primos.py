limite = int(input("Informe o limite: "))

for numero in range(2, limite + 1):
    eh_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            eh_primo = False
            break

    if eh_primo:
        print(numero)