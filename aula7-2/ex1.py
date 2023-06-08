base = int(input("Insira um número de base:"))
potencia = int(input("Insira o valor máximo de potencia:"))
i = 1
resultado = 0

while i <= potencia:
    resultado += base ** i
    i += 1

print(f"O resultado é {resultado}")