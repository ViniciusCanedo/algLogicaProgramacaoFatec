
palavras_invertidas = []


for i in range(20):
    palavra = input("Digite a palavra {}: ".format(i+1))
    palavra_invertida = palavra[::-1]  # Inverter a palavra usando slicing
    palavras_invertidas.append(palavra_invertida)

print("Palavras invertidas:")
for palavra in palavras_invertidas:
    print(palavra)