n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
print("==================================")
print("  ESCOLHA UMA DAS OPÇÕES ABAIXO  ")
print("==================================")
print("(1) Média entre os números")
print("(2) Diferença entre os números")
print("(3) Produto entre os números")
print("(4) Divisão entre os números")
print("==================================")
opcao = int(input("Insira a opção desejada:"))

if(opcao == 1):
    media = (n1 + n2) / 2
    print(f"A média entre {n1} e {n2} é {media}")

elif(opcao == 2):
    verificacao = n1 - n2

    if(verificacao > 0):
        print(f'{n1} - {n2} = número é {n1 - n2}')

    else:
        print(f'{n2} - {n1} = número é {n2 - n1}')

elif(opcao == 3):
    produto = n1 * n2
    print(f"O produto entre {n1} e {n2} é {produto}")

else:
    divisao = n1 / n2
    print(f"A divisão entre {n1} e {n2} é {divisao}")