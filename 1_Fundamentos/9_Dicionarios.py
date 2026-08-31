#Dicionários armazenam informações no formato:
#chave -> valor
pessoa = {
    "nome": "Nicolas",
    "idade": 37,
    "cidade": "Ribeirão Preto"
}

#Podemos acessar os valores através das chaves:
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

#Podemos alterar um valor:
pessoa["idade"] = 21
print(pessoa["idade"])

#Podemos adicionar uma nova informação:
pessoa["profissao"] = "Programador"
print(pessoa)

#Também podemos percorrer um dicionário:
pessoa = {
    "nome": "Nicolas",
    "idade": 20,
    "cidade": "Ribeirão Preto"
}

for chave, valor in pessoa.items():
    print(chave, ":", valor)