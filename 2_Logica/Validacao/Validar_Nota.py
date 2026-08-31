nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 0 and nota <= 10:
    print("Nota valida")
else:
    print("Nota invalida")

#Podemos escrever de uma maneira mais simples
if 0 <= nota <= 10:
    print("Nota valida")
else:
    print("Nota invalida")

#Combinado validações
idade = int(input("Digite sua idade:"))
nota = float(input("Digite sua nota:"))

if idade >= 18 and 0 <= nota <= 10:
    print("Dados validos")
else:
    print("Dados invalidos")