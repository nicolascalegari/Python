#Em cada etapa, escolher a melhor opção disponível naquele momento, esperando chegar a uma solução ótima.
#Queremos usar a menor quantidade possível de moedas.

moedas = [25,10,5,1]
valor = 41

resultado = []

for moeda in moedas:
    while valor >= moeda:
        valor -= moeda
        resultado.append(moeda)

print(resultado)
print("Quantidade:", len(resultado))

#O(n + k)