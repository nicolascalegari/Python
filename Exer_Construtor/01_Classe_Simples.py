class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa_1 = Pessoa("Ana", 25)

print(pessoa_1.nome)
print(pessoa_1.idade)