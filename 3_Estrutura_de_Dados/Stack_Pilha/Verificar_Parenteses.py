expressao = "(10 + 5) * (3 + 2)"

pilha = []

for caractere in expressao:
    if caractere == "(":
        pilha.append(caractere)

    elif caractere == ")":
        if len(pilha) == 0:
            print("Parenteses invalidos")
            break

        pilha.pop()

#Em python o bloco else apos um for so e executado se o laço 
#terminar normalmente(ou seja, se nao passou pelo comando break)
else:
    if len(pilha) == 0:
        print("Parenteses valido")
    else:
        print("Parenteses invalidos")