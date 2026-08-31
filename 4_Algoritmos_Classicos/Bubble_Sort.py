#Algoritmo de ordenação
#Não indicado para grandes listas pela complexidade alta

#Imagine:
#[5, 2, 8, 1]
#Ele compara elementos visinhos
#5 > 2 → troca
#[2, 5, 8, 1]
#8 > 1 → troca
#[2, 5, 1, 8]

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 2, 8, 1, 3]

print(bubble_sort(numeros))

#Detalhes sobre o for j in range(0, n - i - 1):
#0 -> começa pelo indice )
#n -> tamanho da lista
#-i -> remove a quantidade de elementos que já foram ordenados anteriormente
#-1 -> para uma posição antes do fim

#Complexidade O(N²)