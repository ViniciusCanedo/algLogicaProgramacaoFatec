def ler_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def encontrar_maior_elemento(matriz):
    maior = matriz[0][0]
    for i in range(2):
        for j in range(2):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior


def multiplicar_por_maior(matriz, maior):
    matriz_resultante = []
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = matriz[i][j] * maior
            linha.append(elemento)
        matriz_resultante.append(linha)
    return matriz_resultante


def imprimir_matriz(matriz):
    print("Matriz resultante:")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()


matriz = ler_matriz()
maior_elemento = encontrar_maior_elemento(matriz)
matriz_resultante = multiplicar_por_maior(matriz, maior_elemento)
imprimir_matriz(matriz_resultante)
