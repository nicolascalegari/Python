numeros = [8,3,10,2,7]

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(f"Menor: {menor}")

#Esse é um algoritmo muito importante porque o mesmo raciocínio 
#pode ser usado para encontrar máximo, mínimo, maior nota, 
#menor preço etc.