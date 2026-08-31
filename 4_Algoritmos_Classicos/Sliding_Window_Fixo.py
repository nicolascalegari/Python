#Sliding Window significa Janela Deslizante.
#A ideia é analisar uma parte da lista/string de cada vez, evitando recalcular tudo.
#Encontrar a maior soma de 3 números consecutivos.
#[2, 1, 5, 1, 3, 2]
#As janelas são:
#[2, 1, 5] → 8
#[1, 5, 1] → 7
#[5, 1, 3] → 9
#[1, 3, 2] → 6
#Resposta: 9

numeros = [2,1,5,1,3,2]
k = 3

soma = sum(numeros[:k]) #Soma os primeiros k elementos (índices 0, 1 e 2).
maior = soma

for i in range(k, len(numeros)): #O laço vai do índice k (3) até o final da lista. A cada iteração
    soma += numeros[i] #Adiciona o novo elemento que entrou na janela (à direita).
    soma -= numeros[i - k] #Remove o elemento antigo que ficou para trás (à esquerda).
    maior = max(maior, soma) #Atualiza a variável maior caso a soma atual seja superior à anterior.

print("Maior soma:", maior)

#Complexidade
#O(n)