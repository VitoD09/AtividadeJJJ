preco = input("Digite o preço do produto: ")

if preco.strip() == "":
    print("Preço não informado.")
else:
    preco = float(preco)
    quantidade = int(input("Digite a quantidade: "))

    total = preco * quantidade

    print("Total:", total)
