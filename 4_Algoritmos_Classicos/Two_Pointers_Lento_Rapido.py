#Queremos percorrer a lista usando dois ponteiros:
#lento → anda 1 posição por vez
#rápido → anda 2 posições por vez

numeros = [1,2,3,4,5,6,7]

lento = 0
rapido = 0

while rapido < len(numeros):
    print("Lento: ", numeros[lento])
    print("Rapido: ", numeros[rapido])
    print()

    lento += 1
    rapido += 2

#Podemos usar essa técnica para descobrir o elemento do meio de uma lista.

numeros = [10,20,30,40,50,60,70]

lento = 0
rapido = 0

while rapido < len(numeros):
    lento += 1
    rapido += 2

print("Elemento do meio: ", numeros[lento])

#Aqui usamos dois ponteiros que se movimentam em velocidades diferentes.
#É muito comum para descobrir, por exemplo, se uma lista possui um ciclo.
#Existe um ciclo.
#Queremos descobrir se existe esse ciclo.

#1 → 2 → 3 → 4 → 5
#        ↑       ↓
#        ← ← ← ←

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

#Criando os nos
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


#Criando as conexoes
a.proximo = b
b.proximo = c
c.proximo = d
d.proximo = e
e.proximo = c #Cria o ciclo

lento = a
rapido = a

while rapido is not None and rapido.proximo is not None:
    lento = lento.proximo
    rapido = rapido.proximo.proximo

    if lento == rapido:
        print("Ciclo encontrado") 
        break
else:
    print("Nao existe ciclo")

#Complexidade
#Tempo: O(n)
#Memória: O(1)