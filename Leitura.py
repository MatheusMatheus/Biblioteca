def lerInteiro(titulo):
    while True:
        try:
            numero = int(input(titulo))
            return numero
        except ValueError as identifier:
            print("Número inválido\nTente novamente")
        