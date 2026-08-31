numero = int(input("Digite o numero: "))

eh_primo = True

if numero < 2:
    eh_primo = False

for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo:
    print("Primo")
else:
    print("Não é Primo")