#E um dos algoritmos mais importantes para entender eficiencia
#A lista precisa estar ordenada
#Queremos encontrar o 13

#A busca binaria nao verifica todos
#Ela olha para o meio
#1  3  5  7  |9|  11  13  15
#13 e maior que 9 -> procura na metade direita
#11 |13| 15

def busca_binario(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return - 1 #Indica que o elemento procurado nao foi encontrado

numeros = [1, 3, 5, 7, 9, 11, 13, 15] #Lista ordenada

resultado = busca_binario(numeros, 13)

print(resultado)

#Complexidade O(log N)