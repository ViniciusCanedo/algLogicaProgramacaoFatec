while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para encerrar): ")

    if nome_atleta == "":
        break

    saltos = []
    for i in range(1, 6):
        salto = float(input(f"Digite a distância alcançada no {i}º salto: "))
        saltos.append(salto)

    media_saltos = sum(saltos) / 5

    print("\nResultado final:")
    print("Atleta:", nome_atleta)
    print("Saltos:", " - ".join(map(str, saltos)))
    print("Média dos saltos:", media_saltos, "m\n")
