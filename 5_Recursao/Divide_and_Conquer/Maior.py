def maior(lista):

    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    esquerda = maior(lista[:meio])
    direita = maior(lista[meio:])

    return max(esquerda, direita)

numeros = [10,5,30,8,20]

print(maior(numeros))

#Complexidade O(N) Tempo
#Complexidade O(Log N) Espaço