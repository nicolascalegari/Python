def verificar_idade(idade):
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    return f"Idade válida: {idade} anos"

try:
    idade = int(input("Digite a idade: "))
    resul = verificar_idade(idade)
    print(resul)
except ValueError as erro:
    print("Erro:", erro)