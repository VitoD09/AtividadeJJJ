while True:
        try:
            armazem = []
            quantidade = int(input("Informe a quantidade de notas: "))
            if quantidade <= 0:
                print("Informe um valor maior que zero")

            else:        
                for i in range(quantidade):
                    notas = int(input("Digite uma nota: "))
                    armazem.append(notas)

                soma = sum(armazem)
                media = soma/len(armazem)
                print("A media do aluno é: ", media) 
        except ValueError:
             print("Informe um valor numerico")
                

                   
