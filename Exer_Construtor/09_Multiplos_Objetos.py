class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

livros = [
    Livro("Dom Casmurro", "Machado de Assis", 256),
    Livro("O Alquimista", "Paulo Coelho", 208),
    Livro("1984", "George Orwell", 328)
]

for livro in livros:
    print(f"{livro.titulo} - {livro.autor} ({livro.paginas} páginas)")