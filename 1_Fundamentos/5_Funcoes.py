#Função simples
def soma(a, b):
    return a + b

resultado = soma(10, 20)

print(resultado)

#Exemplo mais completo
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

media = calcular_media(8, 9)

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")