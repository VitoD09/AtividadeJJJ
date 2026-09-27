def verificar(idade, renda, cadastro):

    if idade < 18:
        return "Menor de idade"

    elif renda < 1500:
        return "Renda baixa"

    elif cadastro == False:
        return "Cadastro inválido"

    else:
        return "Cadastro aprovado"


print(verificar(16, 2000, True))
print(verificar(20, 1000, True))
print(verificar(20, 2000, False))
print(verificar(20, 2000, True))
