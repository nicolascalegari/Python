def criar_perfil(nome, idade, cidade, **extras):
    perfil = {"nome": nome, "idade": idade, "cidade": cidade}
    perfil.update(extras)
    return perfil

perfil_1 = criar_perfil("Ana", 25, "São Paulo")
perfil_2 = criar_perfil("Bruno", 55, "Curitiba", profissao="Engenheiro", hobby="Xadrez")

print(perfil_1)
print(perfil_2)