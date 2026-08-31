#Uma tabela de frequência registra quantas vezes cada elemento aparece.
#Em Python, normalmente usamos um dict.
#Contar quantas vezes cada número aparece:
#[1, 2, 2, 3, 1, 2, 4]

numeros = [1,2,2,3,1,2,4]

frequencia = {}

for numero in numeros:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

print(frequencia)

#Outro forma
from collections import Counter

numeros = [1,2,2,3,1,2,4]

frequencia = Counter(numeros)

print(frequencia)

#Complexidade
#O(n)