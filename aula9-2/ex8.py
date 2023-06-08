def ler_matriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            elemento = float(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def calcular_media_linhas_pares(matriz):
    soma = 0
    count = 0
    for i in range(1, 5, 2):
        for j in range(5):
            soma += matriz[i][j]
            count += 1
    if count != 0:
        media = soma / count
        return media
    else:
        return 0


matriz = ler_matriz()
media_linhas_pares = calcular_media_linhas_pares(matriz)


print("A média dos elementos nas linhas pares é:", media_linhas_pares)
