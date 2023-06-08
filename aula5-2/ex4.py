x = float(input("Insira o lado x do triângulo: "))
y = float(input("Insira o lado y do triângulo: "))
z = float(input("Insira o lado z do triângulo: "))

if(x < y + z and y < x + z and z < y + x):
    if((x + y + z) / 3 == x):
        print("Esse triângulo é equilátero")
    elif(x == y or y == z or x == z):
        print("Esse triângulo é isósceles")
    else:
        print("Esse triângulo é escaleno")
    
else:
    print("Não é um triângulo")