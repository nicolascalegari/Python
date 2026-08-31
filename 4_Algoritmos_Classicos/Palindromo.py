#Um palíndromo é uma palavra ou frase que permanece igual quando lida de trás para frente.
#Exemplos:
#ovo
#arara
#radar

#Verificar se uma palavra é um palíndromo.

palavra = "radar"

esquerda = 0
direita = len(palavra) - 1

palindromo = True
#Comprar char no inicio com char do final
#r a d a r
#↑       ↑
#Ate chegar ao centro
while esquerda < direita:

    if palavra[esquerda] != palavra[direita]:
        palindromo = False
        break

    esquerda += 1
    direita -= 1

if palindromo:
    print("E palindromo")
else:
    print("Nao e palindrimo")

#Forma mais curta
palavra = "radar"

if palavra == palavra[::-1]:
    print("E palindromo")
else:
    print("Nao e palindromo")
#[::-1] cria uma versão invertida da string.

#Complexidade
#O(n)