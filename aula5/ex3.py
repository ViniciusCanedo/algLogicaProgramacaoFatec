n = int(input("Insira um número inteiro:"))

verificacao = n % 2

if(verificacao == 0 ):
    print(f"{n} é par")

else:
    print(f"{n} é ímpar")