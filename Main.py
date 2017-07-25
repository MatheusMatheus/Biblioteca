from BibliotecaNegocio import BibliotecaNegocio

biblioteca = BibliotecaNegocio()
biblioteca.addLivros()
livro_isbn = biblioteca.selecionaLivro()
biblioteca.realizaReserva(livro_isbn)

biblioteca.mostraLivrosReservados()