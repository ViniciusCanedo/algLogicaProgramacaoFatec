def ler_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            elemento = float(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def calcular_soma_diagonal(matriz):
    soma = 0
    for i in range(4):
        soma += matriz[i][i]
    return soma


matriz = ler_matriz()
soma_diagonal = calcular_soma_diagonal(matriz)

print("A soma dos elementos da diagonal principal é:", soma_diagonal)
