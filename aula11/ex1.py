def carregar_tupla():
    elementos = []
    for i in range(10):
        elemento = int(input("Digite um número inteiro: "))
        elementos.append(elemento)
    tupla = tuple(elementos)
    return tupla


def escrever_tupla_inversa(tupla):
    tupla_inversa = tuple(reversed(tupla))
    return tupla_inversa


tupla_original = carregar_tupla()
tupla_inversa = escrever_tupla_inversa(tupla_original)


print("Tupla na ordem inversa:")
for elemento in tupla_inversa:
    print(elemento)
