salarioMin = float(input("Insira o valor do salario minimo: "))
consumoEnergia = float(input("Insira o consumo de energia (kw): "))
valorKw = salarioMin / 8
total = valorKw * consumoEnergia
desconto = total * 0.85

print(f'O valor do quilowatt é {valorKw} reais, o subtotal é de {total} reais, com desconto de 15% fica {desconto} reais')