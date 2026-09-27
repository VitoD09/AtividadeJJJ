idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")
ano = int(input("Digite o ano: "))

if idade < 0:
    print("Idade inválida.")

elif curso.strip() == "":
    print("Curso não pode ficar vazio.")

elif ano < 1:
    print("Ano inválido.")

else:
    print("Cadastro válido!")
