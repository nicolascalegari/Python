#Um número palíndromo é igual quando lido de trás para frente:
#121, 1331, 1001

numero = 1221

original = numero
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

if original == invertido:
    print("Palindrono")
else:
    print("Não é Palindrono")