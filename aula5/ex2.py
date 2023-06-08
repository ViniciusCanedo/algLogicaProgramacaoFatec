nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))
nota3 = float(input("Insira a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if (media < 3):
    print(f"O aluno foi reprovado com nota {media}")

elif (media < 7):
    print(f"O aluno necessita de uma recuperação devido a nota {media}")

else:
    print(f"O aluno foi aprovado com media {media}")