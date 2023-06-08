def contar_palavra(frase, palavra):
    count = 0


    frase = frase.lower()
    palavra = palavra.lower()

    palavras = frase.split()


    for p in palavras:
        if p == palavra:
            count += 1

    return count

frase = input("Digite uma frase: ")
palavra = input("Digite a palavra a ser contada: ")

resultado = contar_palavra(frase, palavra)
print("Número de vezes que a palavra aparece:", resultado)
