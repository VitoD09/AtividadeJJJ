arquivo = "alunos.txt"

quantidade = int(input("Quantos alunos? "))

with open(arquivo, "a") as f:
    for i in range(quantidade):
        nome = input("Digite o nome: ")
        f.write(nome + "\n")

print("Alunos salvos!")


with open(arquivo, "r") as f:
    alunos = f.readlines()

indice = int(input("Digite a posição do aluno: "))

if 0 <= indice < len(alunos):
    print("Aluno:", alunos[indice].strip())
else:
    print("Essa posição não existe.")
