#Queremos gerar todas as combinações de tamanho 2.

def combinar(numeros, tamanho, atual, resultado):

    if len(atual) == tamanho:
        resultado.append(atual.copy())
        return

    for numero in numeros:

        if numero not in atual:
            atual.append(numero)

            combinar(numeros, tamanho, atual, resultado)

            atual.pop()

numeros = [1,2,3]

resultado = []

combinar(numeros, 2, [], resultado)

print(resultado)

#Visualmente:
#           []
#       /    |    \
#      1     2     3
#     / \   / \   / \
#    12 13 21 23 31 32
#É daí que vem o nome Backtracking:
#Avançar → testar → voltar → testar outra possibilidade.

#O(n!)