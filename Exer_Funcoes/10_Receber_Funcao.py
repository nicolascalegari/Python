def dobrar(numero):
    return numero *  2

def quadrado(numero):
    return numero ** 2

def aplicar(lista, operacao):
    resul = []
    for numero in lista:
        resul.append(operacao(numero))
    return resul

numeros = [1,2,3,4,5]

print(aplicar(numeros, dobrar))
print(aplicar(numeros, quadrado))