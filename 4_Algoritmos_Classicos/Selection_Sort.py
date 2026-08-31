#Procura o menor elemento e coloca na primeira posiçao

#[5, 2, 8, 1, 3]
#menor = 1
#[1, 2, 8, 5, 3]
#Depois procura o menor restante:
#[1, 2, 8, 5, 3]
#    ↑
#E continua

def selection_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i] #Troca -> swap

    return lista

numeros = [10, 8, 6, 5, 3, 1]

print(selection_sort(numeros))

#Complexidade O(N²)