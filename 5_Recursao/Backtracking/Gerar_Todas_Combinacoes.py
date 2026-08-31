#Backtracking significa, basicamente:
#Tentar uma possibilidade → continuar → se não funcionar, voltar atrás e tentar outra.
#Você tenta um caminho. Se encontrar um bloqueio, volta e tenta outro.

def combinar(lista, atual=[]):

    print(atual)

    for elemento in lista:

        if elemento not in atual:

            atual.append(elemento)

            combinar(lista, atual)

            atual.pop()


combinar(["A", "B", "C"])