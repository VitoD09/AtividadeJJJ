nomes = ["João", "Maria", "Pedro", "João", "Ana", "Maria"]

duplicados = []

for nome in nomes:
    if nomes.count(nome) > 1 and nome not in duplicados:
        duplicados.append(nome)

print("Nomes repetidos:", duplicados)
