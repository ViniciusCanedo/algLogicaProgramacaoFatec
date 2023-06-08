def verificar_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


ano = int(input("Digite um ano (formato AAAA): "))

if verificar_ano_bissexto(ano):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
