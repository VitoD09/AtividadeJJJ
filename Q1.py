while True:
    

    try:
        idade = int(input("informe sua idade: "))
        if idade >= 18:
            print("Voce e apto a participar")
            break
        else:
            print("Voce nao tem idade necessaria")  
    except ValueError:
        print("Voce nao digitou um numero valido, por favor tente novamente")
