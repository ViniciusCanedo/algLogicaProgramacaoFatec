def carregar_lista():
    lista = []
    for i in range(10):
        elemento = int(input("Digite um número inteiro: "))
        lista.append(elemento)
    return lista


print("Carregando a primeira lista:")
lista1 = carregar_lista()

print("Carregando a segunda lista:")
lista2 = carregar_lista()

conjunto_uniao = set(lista1).union(lista2)


print("Conjunto da união entre as duas listas:")
print(conjunto_uniao)
