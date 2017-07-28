from BibliotecaNegocio import BibliotecaNegocio
from Emprestimo import Emprestimo

biblioteca = BibliotecaNegocio()
biblioteca.addLivros()
biblioteca.addUsuarios()

usuario = biblioteca.selecionaUsuario()
livro = biblioteca.selecionaLivro()
biblioteca.efetivaEmprestimo(usuario, livro)
#emprestimo = Emprestimo()
#emprestimo.realizaEmprestimo()