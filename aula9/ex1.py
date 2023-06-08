
vetor = []

for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i+1)))
    vetor.append(elemento)


print("Vetor na ordem inversa:")
for i in range(len(vetor)-1, -1, -1):
    print(vetor[i])
