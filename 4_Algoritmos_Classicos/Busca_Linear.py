#Queremos descobrir se 32 esta na lista
#A busca linear verifica um elemento de cada vez

numeros = [10, 25, 7, 32, 15]

procurado = 32

for numero in numeros:
    if numero == procurado:
        print("Encontrado!")
        break

#Complexidade O(N)
#Se tivermos 1 milhao de elementos, no pior caso podemos precisar verificar 1 milhao.

#10 → 25 → 7 → 32
#               ↑
#            encontrado