opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * len(opcoes)

while True:
    voto = int(
        input(
            "Digite o número correspondente ao Sistema Operacional (ou 0 para encerrar)\n1- Windows Server | 2- Unix | 3- Linux | 4- Netware | 5- Mac OS | 6- Outro: "
        )
    )

    if voto == 0:
        break

    if 0 <= voto <= len(opcoes):
        votos[voto - 1] += 1

total_votos = sum(votos)

print("\nSistema Operacional     Votos    %")
print("-------------------     -----   ---")

for i in range(len(opcoes)):
    percentual = (votos[i] / total_votos) * 100
    print(f"{opcoes[i]:<23} {votos[i]:<7} {percentual:.1f}%")

print("-------------------     -----   -----")
print(f"Total                   {total_votos}")

vencedor_index = votos.index(max(votos))
vencedor = opcoes[vencedor_index]
percentual_vencedor = (votos[vencedor_index] / total_votos) * 100

print(
    f"\nO Sistema Operacional mais votado foi o {vencedor}, com {votos[vencedor_index]} votos, correspondendo a {percentual_vencedor:.1f}% dos votos."
)
