#Listas armazenam vários valores em uma única variável. usando []
frutas = ["maçã", "banana", "laranja"]
print(frutas)

#Acessar elementos unicos
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])

#Adicionar elementos usando .appned()
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)

#Remover usando .remove()
frutas.remove("banana")
print(frutas)

#Percorrer uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)