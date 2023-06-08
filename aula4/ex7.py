deposito = float(input("Insira o valor de depósito: "))
taxaJuros = float(input("Insira a taxa de juros (%): "))

taxaJuros /= 100
taxaJuros *= deposito
receitaFinal = deposito + taxaJuros

print(f'O seu dinheiro rendeu R$ {taxaJuros}, totalizando R$ {receitaFinal}')