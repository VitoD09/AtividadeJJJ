senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta!")

if tentativas == 3 and senha != senha_correta:
    print("Número de tentativas excedido.")
