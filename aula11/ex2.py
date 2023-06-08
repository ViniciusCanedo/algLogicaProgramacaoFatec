def carregar_dicionario():
    dicionario = {}
    for i in range(10):
        sobrenome = input("Digite o sobrenome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        dicionario[sobrenome] = idade
    return dicionario


def encontrar_sobrenome_maior_idade(dicionario):
    maior_idade = max(dicionario.values())
    for sobrenome, idade in dicionario.items():
        if idade == maior_idade:
            return sobrenome


dicionario = carregar_dicionario()
sobrenome_maior_idade = encontrar_sobrenome_maior_idade(dicionario)

print("O sobrenome da pessoa com maior idade é:", sobrenome_maior_idade)
