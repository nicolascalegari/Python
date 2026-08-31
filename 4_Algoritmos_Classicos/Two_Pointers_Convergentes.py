#Dada uma lista de números ordenada, encontrar dois números cuja soma seja igual a um determinado valor.
#Exemplo:
#Números: [1, 2, 3, 4, 6]
#Alvo: 6
#A resposta é:
#2 + 4 = 6

numeros = [1,2,3,4,6]
alvo = 6

esquerda = 0
direita = len(numeros) - 1

while esquerda < direita:
    soma = numeros[esquerda] + numeros[direita]

    if soma == alvo:
        print("Encontrado: ", numeros[esquerda], numeros[direita])
        break

    elif soma < alvo:
        esquerda += 1

    else:
        direita -= 1

#Como funciona?
#Temos dois ponteiros:
#[1, 2, 3, 4, 6]
# ↑           ↑
#esquerda   direita
#Calculamos:
#1 + 6 = 7
#É maior que 6, então diminuímos o ponteiro da direita:
#[1, 2, 3, 4, 6]
# ↑        ↑
#Agora:
#1 + 4 = 5
#É menor que 6, então aumentamos o ponteiro da esquerda:
#[1, 2, 3, 4, 6]
#    ↑     ↑
#Agora:
#2 + 4 = 6
#Encontramos!
#Complexidade:
#O(n) — cada ponteiro percorre a lista no máximo uma vez.