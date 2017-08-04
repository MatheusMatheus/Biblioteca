from BibliotecaNegocio import BibliotecaNegocio
from Leitura import lerInteiroLimite as inteiro

class Emprestimo(object):
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.livros = [] 
        self.dataInicial = None
        self.dataFinal = None
        self.usuario = None
       
    def realizaEmprestimo(self):
        self.usuario = self.biblioteca.selecionaUsuario()
        self.livros = self.escolherLivros()
        self.biblioteca.efetivaEmprestimo(self.usuario, self.livros)

    def escolherLivros(self):
        livros = []
        while True:
            livros.append(self.biblioteca.selecionaLivro())
            opcao = inteiro("Deseja selecionar outro livro?\n1-Sim\n0-não\nOpção: ", 0, 1)
            if opcao == 0:
                return livros