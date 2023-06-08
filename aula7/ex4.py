n = "start"
soma = 0
for i in n:
    n = int(input("Digite um número par para somar. Digite 0 para finalizar a soma e exibir o valor.Números ímpares serão desconsiderados: "))

    if(n % 2 == 0 and n != 0):
        soma += n
    elif(n == 0):
        break

print(f"O valor final é {soma}")