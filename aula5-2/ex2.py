idade = int(input("Insira sua idade: "))

if(idade < 8):
    print("Você está na categoria infantil")

elif(idade < 11):
    print("Você está na categoria juvenil")

elif(idade < 16):
    print("Você está na categoria adolescente")

elif(idade < 31):
    print("Você está na categoria adulto")

else:
        print("Você está na categoria sênior")