def ler_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(20):
            elemento = int(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def calcular_somas_linhas(matriz):
    somas = []
    for linha in matriz:
        soma = sum(linha)
        somas.append(soma)
    return somas


def multiplicar_por_soma_linha(matriz, somas):
    matriz_resultante = []
    for i in range(10):
        linha_resultante = []
        for j in range(20):
            elemento = matriz[i][j] * somas[i]
            linha_resultante.append(elemento)
        matriz_resultante.append(linha_resultante)
    return matriz_resultante


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()


matriz = ler_matriz()
somas_linhas = calcular_somas_linhas(matriz)
matriz_resultante = multiplicar_por_soma_linha(matriz, somas_linhas)

print("Matriz resultante:")
imprimir_matriz(matriz_resultante)
