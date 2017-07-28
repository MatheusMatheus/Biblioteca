from BibliotecaNegocio import BibliotecaNegocio
from Emprestimo import Emprestimo

biblioteca = BibliotecaNegocio()

biblioteca.addLivros()
biblioteca.addUsuarios()

emprestimo = Emprestimo(biblioteca)
emprestimo.realizaEmprestimo()