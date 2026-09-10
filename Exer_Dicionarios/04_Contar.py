frase = "o gato subiu no telhado e o gato desceu"
palavras = frase.split()
frequencia = {}

for palavra in palavras:

    if palavra in frequencia:

        frequencia[palavra] += 1

    else:

        frequencia[palavra] = 1

print(frequencia)