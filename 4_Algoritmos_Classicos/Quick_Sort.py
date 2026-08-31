#Estrategia Dividir e Conquistar
#Escolhe um elemento chamado pivo e divide os elementos em:
#Menores que o pivo | pivo | Maiores que o pivo
#Exemplo:
#[8, 3, 5, 1, 7]
#Escolhendo 5 como pivo:
#[3, 1] | 5 | [8, 7]
#Depois e feito a mesma coisa com as duas partes

def quick_sort(lista):

    #Caso base, se a lista tiver 1 ou 0 elementos, retorno imediato
    if len(lista) <= 1:
        return lista

    #Escolhe o pivo
    pivo = lista[len(lista) // 2]

    #Divide os elementos
    menores = []
    iguais = []
    maiores = []

    for x in lista: #Abaixo uma forma mais elegange de escreve esse for
        if x < pivo:
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else:
            maiores.append(x)

    #Ordena recursivamente
    return quick_sort(menores) + iguais + quick_sort(maiores)

numeros = [8,3,5,1,9,2,7,4]

resultado = quick_sort(numeros)

print(resultado)

#Complexidade: O(N²)

#Outra forma de escrever o for usando menos linhas
#Usando List Comprehension

#menores = [x for x in lista if x < pivo]
#iguais = [x for x in lista if x == pivo]
#maiores = [x for x in lista if x > pivo]