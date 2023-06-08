n1 = int(input("Insira um número:"))
n2 = int(input("Insira um segundo número:"))

verificacao = n1 - n2

if(verificacao > 0):
    print(f'o maior número é {n1}')

else:
    print(f'o maior número é {n2}')