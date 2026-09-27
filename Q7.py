identificador = input("Digite o identificador: ")

if len(identificador) == 11 and identificador.isdigit():
    print("Identificador válido")
else:
    print("Identificador inválido")
