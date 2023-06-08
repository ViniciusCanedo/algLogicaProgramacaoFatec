
vetor1 = []
vetor2 = []


print("Carregando elementos do vetor 1:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i+1)))
    vetor1.append(elemento)


print("Carregando elementos do vetor 2:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i+1)))
    vetor2.append(elemento)


vetor_resultante = []
for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])

print("Vetor resultante:")
for elemento in vetor_resultante:
    print(elemento)
