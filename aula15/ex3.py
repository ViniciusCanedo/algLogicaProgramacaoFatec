numero = int(input("Digite um número inteiro positivo: "))

numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", numero_invertido)
