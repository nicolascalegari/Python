palavra = input("Digite uma palavra: ")

for indice, letra in enumerate(palavra):

    if indice % 2 != 0:

        print(f"Posição {indice}: {letra}")