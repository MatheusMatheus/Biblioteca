from BibliotecaNegocio import BibliotecaNegocio

class Emprestimo:
    def __init__(self):
        self.codigoEmprest = None
        self.usuario = None
        self.livros = None
        self.dataInicial = None
        self.dataFinal = None
        self.livros = None


    def realizaEmprestimo(self):
        biblioteca = BibliotecaNegocio()
        usuario = biblioteca.selecionaUsuario()
        livro = biblioteca.selecionaLivro()
        biblioteca.efetivaEmprestimo(usuario, livro)
           
        