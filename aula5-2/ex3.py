preco = float(input("Insira o valor do produto: "))
origem = int(input("Insira o código de origem (somente valores de 1 a 5): "))

if(origem == 1):
    print(f"O valor do produto vindo do sul é de R$ {preco * 1.11}")

elif(origem == 2):
    print(f"O valor do produto vindo do norte é de R$ {preco * 1.13}")

elif(origem == 3):
    print(f"O valor do produto vindo do nordeste é de R$ {preco * 1.09}")

elif(origem == 4):
    print(f"O valor do produto vindo do centro-oeste é de R$ {preco * 1.12}")

else:
    print(f"O valor do produto vindo do sudeste é de R$ {preco * 1.18}")