status_aluno = lambda nota: "Aprovado" if nota >= 7 else ("Recuperação" if nota >= 5 else "Reprovado")

print(f"Nota: 3 {status_aluno(8)}")
print(f"Nota: 6 {status_aluno(6)}")
print(f"Nota: 3 {status_aluno(3)}")