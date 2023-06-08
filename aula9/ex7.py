def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros_primos = []
numero = 101  # Começando a busca a partir de 101, o primeiro primo acima de 100

while len(numeros_primos) < 10:
    if eh_primo(numero):
        numeros_primos.append(numero)
    numero += 1

print(numeros_primos)
