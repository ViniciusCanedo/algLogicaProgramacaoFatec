def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = float(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def criar_matriz_transposta(matriz):
    matriz_transposta = []
    for j in range(3):
        linha_transposta = []
        for i in range(3):
            elemento = matriz[i][j]
            linha_transposta.append(elemento)
        matriz_transposta.append(linha_transposta)
    return matriz_transposta


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()


matriz = ler_matriz()
matriz_transposta = criar_matriz_transposta(matriz)

print("Matriz transposta:")
imprimir_matriz(matriz_transposta)
