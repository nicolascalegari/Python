texto = """Python é uma lingugem versátil.
Ela é usada em ciência de dados.
Também é usada em desenvolvimento web."""

linhas = texto.split("\n")

for numero, linha in enumerate(linhas, start=1):

    print(f"{numero}: {linha}")