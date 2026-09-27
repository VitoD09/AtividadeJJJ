try:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 2

    if idade < 0:
        print("Idade inválida.")

    elif media >= 7:
        print("Aluno aprovado!")

    elif media >= 5:
        print("Aluno em recuperação.")

    else:
        print("Aluno reprovado.")

except ValueError:
    print("Digite valores válidos.")
