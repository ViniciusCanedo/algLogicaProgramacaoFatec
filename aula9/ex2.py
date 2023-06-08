
vetor = []


for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i+1)))
    vetor.append(elemento)


maior_valor = vetor[0]
posicao_maior_valor = 0
for i in range(1, len(vetor)):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
        posicao_maior_valor = i


print("Maior valor:", maior_valor)
print("Posição:", posicao_maior_valor)
