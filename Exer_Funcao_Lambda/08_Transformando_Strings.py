palavras = ['python', 'lambda', 'programacao']

# Usando lamda com metodo .upper() das strings
maiusculas = list(map(lambda p: p.upper(), palavras))

print(f"Palavras em maiúsculas: {maiusculas}")