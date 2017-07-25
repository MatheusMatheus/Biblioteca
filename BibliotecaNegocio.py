from Livro import Livro
import random
import Leitura

class BibliotecaNegocio:
    def __init__(self, usuarios=None, livrosReservados=None, livrosDisponiveis=None):
        self.usuarios = {} if usuarios is None else usuarios
        self.livrosReservados = {} if livrosReservados is None else livrosReservados
        self.livrosDisponiveis = {} if livrosDisponiveis is None else livrosDisponiveis

    def addLivros(self):
        for i in range(0,100):
            livro = Livro(
                "isbn-{}".format(str(random.randrange(30000, 90000))), 
                "titulo-{}".format(str(i)),
                "autor{}".format(str(i)),
                "codigo-{}".format(str(random.randrange(300, 30000))),
                False)

            self.livrosDisponiveis.update({livro.isbn : livro})

    def realizaReserva(self, isbn):
        encontrado = False
        isbn = "isbn-" + str(isbn)
        for k in self.livrosDisponiveis.keys():
            if isbn in self.livrosDisponiveis:
                self.livrosReservados[isbn] = self.livrosDisponiveis.pop(isbn)
                encontrado = True
                break

        if not encontrado:
            print("Livro {} não encontrado".format(isbn))
        

    def mostraLivrosDisponiveis(self):
        for k, v in self.livrosDisponiveis.items():
            print("{} - {}".format(k, v)) 

    def mostraLivrosReservados(self):
        for k, v in self.livrosReservados.items():
            print("{} - {}".format(k, v.titulo)) 

    def selecionaLivro(self):
        for livro in self.livrosDisponiveis.values():
            print("{} - {}".format(livro.isbn, livro.titulo))
        num_livro = int(Leitura.lerInteiro("Informe o número ISBN do livro desejado: "))
        return num_livro



        
        