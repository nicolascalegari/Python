#set representa um conjunto de valores únicos. usando {}
numeros = {1, 2, 3, 4, 5}
print(numeros)

#Uma característica importante é que ele não permite valores duplicados:
numeros = {1, 2, 2, 3, 3, 4}
print(numeros)

#Podemos adicionar usando .add()
numeros = {1, 2, 3}
numeros.add(4)
print(numeros)

#E remover usando .remove()
numeros.remove(2)
print(numeros)

#Exemplo interessante
#Imagine duas listas de alunos:
turma_a = {"João", "Maria", "Carlos"}
turma_b = {"Maria", "Carlos", "Pedro"}
#Podemos descobrir quem está nas duas turmas:
print(turma_a & turma_b)