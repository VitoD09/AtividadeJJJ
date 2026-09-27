try:
    arquivo = open("alunos.txt", "r")

    print(arquivo.read())

    arquivo.close()

except FileNotFoundError:
    print("Erro: o arquivo alunos.txt não foi encontrado.")
