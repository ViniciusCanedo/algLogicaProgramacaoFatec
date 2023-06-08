idade = True
somaIdade = 0
count = 0

while idade != 0 :
    idade = int(input("Insira uma idade para somar. Digite 0 para encerrar a soma e exibir o resultado: "))

    if(idade != 0):
      somaIdade += idade
      count += 1

mediaIdade = somaIdade / count

print(f'Em uma pesquisa feita com {count} pessoas, tivemos uma média de idade de {mediaIdade} anos')