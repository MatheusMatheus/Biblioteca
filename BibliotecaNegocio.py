import Livro

class BibliotecaNegocio:
    def __init__(self, usuarios=None, livrosReservados=None, livrosDisponiveis=None):
        self.usuarios = {} if usuarios is None else usuarios
        self.livrosReservados = {} if livrosReservados is None else livrosReservados
        self.livrosDisponiveis = {} if livrosDisponiveis is None else livrosDisponiveis

    @classmethod
    def addLivros(cls):
        for i in range(0,100):
            titulo = "livro-" + str(i)
            cls.livrosDisponiveis.update({titulo : Livro.isbn})

    def mostraLivros(cls):
        for k, v in cls.livrosDisponiveis:
            print("{} - {}".format(k, v)) 


biblioteca = BibliotecaNegocio()
biblioteca.addLivros()
biblioteca.mostraLivros() 
        
        