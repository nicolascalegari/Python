# Funcao lambda com dois parametros
soma = lambda a, b: a + b
a, b = map(int,input("Digite dois valores: ").split())

resultado = soma(a, b)
print(f"A soma é: {resultado}")