import Livro
class Usuario:

    def __init__(self, matricula, nome, email, endereco, telefone, livros=None):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
        self.livros = {} if livros is None else livros

    def __str__(self):
        return "\nMatrícula {}\n\t{}\n\t{}\n\t{}\n\t{}\n".format(self.matricula, self.nome, self.email, self.endereco, self.telefone)

''' 
    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, nome):
        self.email = "{}@email.com".format(nome) '''
        