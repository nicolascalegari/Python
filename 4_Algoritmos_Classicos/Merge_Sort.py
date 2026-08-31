#Estrategia Dividir e Conquistar
#Divide a lista no meio e continua dividindo ate sobrar um elemento
#Junta as partes novamento ja ordenado

def merge_sort(lista): #Divide

    #Caso base, se a lista tiver 1 ou 0 elementos, retorno imediato
    if len(lista) <= 1:
        return lista

    #Divide a lista no meio
    meio = len(lista) // 2

    esquerda = lista[:meio] #Recebe do meio para esquerda da lista
    direita = lista[meio:] #Recebe do meio para direita da lista

    #Ordena recursivamente cada metade para continuar a divisao
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    #Junta as duas partes ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita): #Junta
    resultado = []

    i = 0
    j = 0

    #Compara os elementos das duas listas
    while i < len(esquerda) and j < len(direita):

        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    #Adiciona o que sobrou da direita
    resultado.extend(esquerda[i:])
    #Adiciona o que sobrou da esquerda
    resultado.extend(direita[j:])

    return resultado

numeros = [8, 3, 5, 1, 6, 2, 7, 4]

resultado = merge_sort(numeros)

print(resultado)

#Complexidade O(N log N)