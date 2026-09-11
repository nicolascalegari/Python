try:
    num_1 = float(input())
    num_2 = float(input())
    resul = num_1 / num_2
    print("Resultado: ", resul)
except ZeroDivisionError:
    print("Erro: Divisão por Zero!")