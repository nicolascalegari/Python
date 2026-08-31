#Duas palavras são anagramas quando possuem as mesmas letras na mesma quantidade, mas podem estar em ordem diferente.
#Exemplo:
#amor
#roma

#Verificar se duas palavras são anagramas.

#Resolução usando tabela de frequência
palavra1 = "amor"
palavra2 = "roma"

frequencia1 = {}
frequencia2 = {}

for letra in palavra1:
    if letra in frequencia1:
        frequencia1[letra] += 1
    else:
        frequencia1[letra] = 1

for letra in palavra2:
    if letra in frequencia2:
        frequencia2[letra] += 1
    else:
        frequencia2[letra] = 1

if frequencia1 == frequencia2:
    print("Sao anagramas")
else:
    print("Nao sao anagramas")

#Forma mais simples
#Ordenando as letras

palavra1 = "amor"
palavra2 = "roma"

if sorted(palavra1) == sorted(palavra2):
    print("Sao anagramas")
else:
    print("Nao sao anagramas")

#Complexidade:

#Com sorted():
#O(n log n)

#Com tabela de frequência:
#O(n)