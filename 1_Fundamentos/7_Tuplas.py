#Tuplas são parecidas com listas, mas são imutáveis. usando ()
cores = ("vermelho", "verde", "azul")
print(cores)

#Podemos acessar elementos
print(cores[0])
print(cores[1])

#Mas não podemos alterar
cores = ("vermelho", "verde", "azul")
# Isso gera erro:
cores[0] = "amarelo"

#Lista  → pode ser modificada
#Tupla  → não pode ser modificada