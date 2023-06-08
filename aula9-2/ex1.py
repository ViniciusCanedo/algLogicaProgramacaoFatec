
def ler_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f"Digite o valor para [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_elementos(matriz):
    print("Ordem dos elementos:")
    print(f"1,1 = {matriz[0][0]}")
    print(f"1,2 = {matriz[0][1]}")
    print(f"2,1 = {matriz[1][0]}")
    print(f"2,2 = {matriz[1][1]}")

matriz = ler_matriz()
imprimir_elementos(matriz)