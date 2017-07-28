class Livro:

    def __init__(self, isbn, titulo, autor, codigoSessao, emprestado):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.codigoSessao = codigoSessao
        self.emprestado = emprestado

    def __str__(self):
        return "\nISBN {}\n\t{}\n\t{}\n\t{}\n".format(self.isbn, self.titulo, self.autor, self.codigoSessao)
