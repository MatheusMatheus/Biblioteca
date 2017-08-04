from Livro import Livro
from Usuario import Usuario

import random
import os

import Leitura

class BibliotecaNegocio:
    def __init__(self, usuarios=None, livrosReservados=None, livrosDisponiveis=None):
        self.usuarios = {} if usuarios is None else usuarios
        self.livrosReservados = {} if livrosReservados is None else livrosReservados
        self.livrosDisponiveis = {} if livrosDisponiveis is None else livrosDisponiveis

    def addUsuarios(self):
        for i in range(0,100):
            matricula = random.randrange(30000, 90000)
            nome = "user-{}".format(str(random.randrange(30000,90000)))
            email = "{}@email.com".format(nome)
            tel1 = random.randrange(3000, 5000)
            tel2 = random.randrange(4000, 6000)
            telefone = "{}-{}".format(tel1, tel2)
            end = random.randrange(10,500)
            endereco = "Rua {} Casa {}".format(str(end), str(end * 3))
            
            user = Usuario(matricula, nome, email, endereco, telefone)
            self.usuarios.update({user.matricula : user})



    def addLivros(self):
        for i in range(0,100):
            isbn = random.randrange(3000000, 9000000)
            titulo = "titulo-{}".format(str(i))
            autor = "autor{}".format(str(i))
            codigo = "codigo-{}".format(str(random.randrange(300, 30000)))
            emprestado = False

            livro = Livro(isbn, titulo, autor, codigo, emprestado)
            self.livrosDisponiveis.update({livro.isbn : livro})



    def efetivaEmprestimo(self, usuario, livrosSelecionados):
        encontrado = False
        for livSelect in livrosSelecionados:
            for livsDisp in self.livrosDisponiveis:
                if livSelect is livsDisp:
                    self.livrosReservados[livsDisp] = self.livrosDisponiveis.pop(livsDisp)
                    self.livrosReservados[livsDisp].emprestado = True
                    encontrado = True
                    usuario.livros = livrosSelecionados
       


    def validaUsuario(self, usuario):
        return True if usuario in self.usuarios else False



    def mostraLivrosDisponiveis(self):
        for k, v in self.livrosDisponiveis.items():
            print("{} - {}".format(k, v)) 



    def mostraLivrosReservados(self):
        for k, v in self.livrosReservados.items():
            print("{} - {}".format(k, v.titulo)) 



    def mostraUsuarios(self):
        for k, v in self.usuarios.items():
            print("{} - {}".format(k, v))



    def selecionaUsuario(self):
        while True:
            self.mostraUsuarios()
            matricula = int(Leitura.lerInteiro("Selecione um aluno por sua matrícula: "))
            if matricula in self.usuarios.keys():
                return matricula
            else:
                print("Matrícula não encontrada\nTente novamente\n")
                os.system("pause")    
                os.system("cls")    
                                

    def selecionaLivro(self):
        while True:
            self.mostraLivrosDisponiveis()
            isbn = int(Leitura.lerInteiro("Informe o ISBN do livro: "))
            if isbn in self.livrosDisponiveis.keys():
                return isbn
            else:
                print("ISBN não encontrado\nTente novamente\n")
                os.system("pause")    
                os.system("cls")   

