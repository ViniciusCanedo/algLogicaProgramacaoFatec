def verificar_palindromo(vetor):
    tamanho = len(vetor)
    for i in range(tamanho // 2):
        if vetor[i] != vetor[tamanho - 1 - i]:
            return False
    return True

# Solicita ao usuário que digite o vetor
vetor = input("Digite os elementos do vetor separados por espaço: ").split()

# Verifica se o vetor é um palíndromo
resultado = verificar_palindromo(vetor)

# Exibe o resultado
if resultado:
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")
