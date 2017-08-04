import Livro
class Usuario:

    def __init__(self, matricula, nome, email, endereco, telefone):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    @property
    def livros(self):
        return self.livros

    @livros.setter
    def livros(self, livros):
        self.livros = livros

    def __str__(self):
        return "\nMatrícula {}\n\t{}\n\t{}\n\t{}\n\t{}\n".format(self.matricula, self.nome, self.email, self.endereco, self.telefone)


        