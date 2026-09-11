L = ["Maça", "Banana", "Uva"]

try:
    i = int(input("Digite um indice para a lista: "))
    print("Fruta:", L[i])
except IndexError:
    print("Erro! Indice inexistente!")
except ValueError:
    print("Erro! Digite apenas numeros inteiros.")