import os


def lerInteiro(titulo):
    while True:
        try:
            numero = int(input(titulo))
            return numero
        except ValueError as ve:
            print("Número inválido\nTente novamente")


def lerInteiroLimite(titulo, min, max):
    while True:
        numero = lerInteiro(titulo)
        if( numero < min or numero > max):
            print("O numero deve estar entre {} e {}\n".format(min, max))
            os.system("pause")
            os.system("cls")
        else:
            return numero


        