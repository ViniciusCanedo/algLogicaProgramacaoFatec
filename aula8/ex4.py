def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    count = 0

    frase = frase.lower()


    for caractere in frase:
        if caractere in vogais:
            count += 1

    return count


frase = input("Digite uma frase: ")


resultado = contar_vogais(frase)
print("Número de vogais:", resultado)
