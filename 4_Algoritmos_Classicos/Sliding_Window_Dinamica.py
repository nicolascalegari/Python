#Aqui o tamanho da janela pode aumentar ou diminuir.
#Encontrar o menor trecho de uma lista cuja soma seja maior ou igual a 7.
#[2, 3, 1, 2, 4, 3]
#Uma possível resposta: [4, 3]
#Tamanho = 2

numeros = [2,3,1,2,4,3]
alvo = 7

esquerda = 0
soma = 0
menor = float("inf") #Valor infinitamente positivo

for direita in range(len(numeros)): #Acumula ate chegar no valor alvo e entrar no while
    soma += numeros[direita]

    while soma >= alvo:
        tamanho = direita - esquerda + 1
        menor = min(menor, tamanho)
        soma -= numeros[esquerda]
        esquerda += 1

print("Menor tamanho: ", menor)

#Complexidade
#O(n)
#Apesar de existir um while dentro do for, cada elemento entra e sai da janela no máximo uma vez.