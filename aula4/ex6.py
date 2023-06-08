salarioAtual = float(input("Insira o salário atual: "))
porcentagemAumento = float(input("Insira a porcentagem de aumento: "))

porcentagemAumento /= 100
porcentagemAumento *= salarioAtual
novoSalario = salarioAtual + porcentagemAumento

print(f'O novo salário é R$ {novoSalario}, com um aumento de R$ {porcentagemAumento}')