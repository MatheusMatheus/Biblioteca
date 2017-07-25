class Emprestimo:
    def __init__(self, codigoEmprest, usuario, livros, dataInicial, dataFinal):
        self.codigoEmprest = codigoEmprest
        self.usuario = usuario
        self.livros = livros
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        self.livros = [] if livros is None else livros

        