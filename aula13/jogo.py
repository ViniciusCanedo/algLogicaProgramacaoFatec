import funcoes


def jogo_de_dados():
    meu_valor = funcoes.rolar_dado()
    valor_computador = funcoes.rolar_dado()

    print("Seu valor:", meu_valor)
    print("Valor do computador:", valor_computador)

    if meu_valor > valor_computador:
        print("Você venceu!")
    elif meu_valor < valor_computador:
        print("O computador venceu!")
    else:
        print("Empate!")


jogo_de_dados()
