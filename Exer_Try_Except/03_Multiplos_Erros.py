try:
    num_1 = float(input("Primeiro numero: "))
    num_2 = float(input("Segundo numero: "))
    resul = num_1 / num_2
    print("Resultado:", resul)
except ValueError:
    print("Erro! Digite apenas numeros.")
except ZeroDivisionError:
    print("Erro! Divisão por zero!")