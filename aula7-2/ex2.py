base = int(input("Insira um número de base do triangulo: "))
while base <= 0:
    base = int(input("Insira um número de base do triangulo: "))


altura = int(input("Insira o valor da altura do triangulo: "))
while base <= 0:
    altura = int(input("Insira o valor da altura do triangulo: "))

area = (base * altura) / 2

print(f"A área do triângulo é {area} m²")