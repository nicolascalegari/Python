#Somando [1,2,3,4]
#[1,2] [3,4]
#[1] [2] [3] [4]
#1 + 2 = 3
#3 + 4 = 7
#3 + 7 = 10

def soma(lista):

    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    esquerda = lista[:meio]
    direita = lista[meio:]

    soma_esquerda = soma(esquerda)
    soma_direita = soma(direita)

    return soma_esquerda + soma_direita

numeros = [1,2,3,4]

print(soma(numeros))

#Complexidade O(N)