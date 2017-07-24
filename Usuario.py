import Livro
class Usuario:

    def __init__(self, matricula, nome, email, endereco, telefone):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    @emprestimo.setter
    def emprestimo(self):
