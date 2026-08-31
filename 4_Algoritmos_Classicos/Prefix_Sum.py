#Prefix Sum significa Soma de Prefixos.
#A ideia é pré-calcular somas para responder rapidamente perguntas do tipo:
#"Qual é a soma dos elementos entre as posições X e Y?"
#Dada a lista:
#[2, 4, 6, 8, 10]
#Queremos descobrir rapidamente a soma entre os índices 1 e 3:
#4 + 6 + 8 = 18

numeros = [2,4,6,8,10]
prefixo = [0]

for numero in numeros:
    prefixo.append(prefixo[-1] + numero)

print(prefixo)

#Agora podemos fazer a consulta:
esquerda = 1
direita = 3

soma = prefixo[direita + 1] - prefixo[esquerda]

print(soma)

#Complexidade
#Construção:
#O(n)
#Cada consulta:
#O(1)