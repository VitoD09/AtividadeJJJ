nota = float(input("Digite a nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado")

elif nota >= 5 and nota < 7:
    print("Recuperação")

elif nota >= 0 and nota < 5:
    print("Reprovado")

else:
    print("Nota inválida")
