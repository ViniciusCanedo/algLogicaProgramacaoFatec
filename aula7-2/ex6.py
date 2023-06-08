n = int(input("Insira um número inteiro para fatorial: "))
fatorial = n

i = n - 1

while i > 0:
    n *= (i)
    i -= 1

print (f"O valor de {fatorial}! é {n}")