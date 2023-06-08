def ler_matriz():
    matriz = []
    for i in range(8):
        linha = []
        for j in range(8):
            elemento = int(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def verificar_simetria(matriz):
    for i in range(8):
        for j in range(8):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


matriz = ler_matriz()
simetrica = verificar_simetria(matriz)


if simetrica:
    print("A matriz digitada é simétrica.")
else:
    print("A matriz digitada não é simétrica.")
