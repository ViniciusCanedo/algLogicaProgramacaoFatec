def ler_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            elemento = int(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def encontrar_posicao_maior(matriz):
    maior = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0
    for i in range(10):
        for j in range(10):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                linha_maior = i
                coluna_maior = j
    return linha_maior, coluna_maior


matriz = ler_matriz()
linha_maior, coluna_maior = encontrar_posicao_maior(matriz)


print("A posição do maior elemento é:", (linha_maior + 1, coluna_maior + 1))
