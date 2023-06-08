n = int(input("Insira um número inteiro para fatorial: "))
fatorial = n

for i in range(fatorial, 1, -1):
    n = n * (i -1)

print (f"O valor de {fatorial}! é {n}")