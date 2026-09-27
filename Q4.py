try:
    preco = input("Digite o preço da compra: ")

    preco = float(preco)

    quantidade = int(input("Digite a quantidade: "))

    total = preco * quantidade

    print("Valor total da compra: R$", total)

except ValueError:
    print("Erro: digite apenas números válidos.")
