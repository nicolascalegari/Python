class Turma:

    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []

    def adicionar(self, nome_aluno):
        self.alunos.append(nome_aluno)

turma_1 = Turma("Python Básico")
turma_1.adicionar("Ana")
turma_1.adicionar("Bruno")

print(f"Turma: {turma_1.nome_turma}")
print(f"Alunos: {turma_1.alunos}")