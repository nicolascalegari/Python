frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para procurar: ")

frase = frase.lower()
palavra = palavra.lower()

contador = frase.count(palavra)

if contador > 0:
    print("Palavra econtrada")
    print("Quantidade de vezes: ", contador)
else:
    print("Palvra nao encontrada")
