palavras = ["python", "java", "python", "c", "python", "java"]

contador = {} #Dicionario vazio

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print(contador)