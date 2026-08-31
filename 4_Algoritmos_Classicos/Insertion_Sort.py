#Parecido com organizar cartas na mao

#Imagine:
#[5, 2, 4, 1]
#Pegamos o 2:
#5  2
#Como 2 e menor que 5:
#2  5
#Depois pegamos o 4:
#2  5  4
#Resultado:
#2  4  5

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

numeros = [5, 2, 4, 1]

print(insertion_sort(numeros))

#Complexida: Pior caso: O(N²)