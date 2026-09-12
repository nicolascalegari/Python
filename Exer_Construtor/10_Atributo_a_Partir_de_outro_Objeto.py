class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Empresa:

    def __init__(self, empresa, funcionarios):
        self.empresa = empresa
        self.funcionarios = funcionarios
        self.folha_pagamento =sum(f.salario for f in funcionarios)

funcionarios = [
    Funcionario("Ana", 3500),
    Funcionario("Bruno", 4200),
    Funcionario("Carla", 3900)
]

empresa_1 = Empresa("Tech Solutions", funcionarios)
print(f"Empresa: {empresa_1.empresa}")
print(f"Folha de pagamento total: R$ {empresa_1.folha_pagamento:.2f}")