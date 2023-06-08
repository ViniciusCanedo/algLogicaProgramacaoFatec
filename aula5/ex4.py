sexo = input("Insira seu sexo (M/H): ")
altura = float(input("Insira sua altura (Ex: 1.75): "))

if sexo == "M":
    pesoIdeal = 62.1 * altura - 44.7
    print(pesoIdeal)

elif sexo == "H":
    pesoIdeal = 72.7 * altura - 58
    print(pesoIdeal)

else:
    print("Sexo inválido")
