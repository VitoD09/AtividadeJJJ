valor = float(input("Digite o valor da compra: R$ "))

if valor < 0:
    print("Valor inválido.")

elif valor > 100:
    desconto = valor * 0.10
    total = valor - desconto
    print("Total:", total)

else:
    print("Total:", valor)
  
