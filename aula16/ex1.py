def validar_sobrenome(sobrenome):
    return sobrenome.strip() != ""


def validar_idade(idade):
    return idade.isdigit()


def validar_altura(altura):
    return altura.isdigit()


def validar_peso(peso):
    try:
        float(peso)
        return True
    except ValueError:
        return False


dados_pessoais = []

while True:
    sobrenome = input("Digite o sobrenome: ")
    if not validar_sobrenome(sobrenome):
        break

    idade = input("Digite a idade: ")
    if not validar_idade(idade):
        print("Idade inválida. Por favor, digite um número inteiro.")
        continue

    altura = input("Digite a altura (em centímetros): ")
    if not validar_altura(altura):
        print("Altura inválida. Por favor, digite um número inteiro.")
        continue

    peso = input("Digite o peso (em kg): ")
    if not validar_peso(peso):
        print("Peso inválido. Por favor, digite um número válido.")
        continue

    dados_pessoais.append(
        {
            "sobrenome": sobrenome,
            "idade": int(idade),
            "altura": int(altura),
            "peso": float(peso),
        }
    )

dados_pessoais.sort(key=lambda x: x["sobrenome"])

print("\nListagem de dados pessoais:")
for pessoa in dados_pessoais:
    print(f"Sobrenome: {pessoa['sobrenome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Altura: {pessoa['altura']} cm")
    print(f"Peso: {pessoa['peso']} kg")
    print()

media_idade = sum(pessoa["idade"] for pessoa in dados_pessoais) / len(dados_pessoais)
media_altura = sum(pessoa["altura"] for pessoa in dados_pessoais) / len(dados_pessoais)
media_peso = sum(pessoa["peso"] for pessoa in dados_pessoais) / len(dados_pessoais)

print("Resumo:")
print(f"Média da idade: {media_idade:.2f} anos")
print(f"Média da altura: {media_altura / 100:.2f} m")
print(f"Média do peso: {media_peso:.2f} kg")
