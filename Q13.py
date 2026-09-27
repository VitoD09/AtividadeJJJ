temperaturas = [25, 18, 30, -2, 30, 22]

maior = temperaturas[0]
menor = temperaturas[0]

for temperatura in temperaturas:
    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
