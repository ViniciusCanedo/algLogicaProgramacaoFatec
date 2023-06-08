dataNasc = int(input("Insira o ano de nascimento:"))
dataAtual = int(input("Insira o ano atual:"))

idade = dataAtual - dataNasc

if (idade >= 16):
  resultado = "Você pode votar"
  if (idade >= 18):
    resultado += " e pode tirar habilitação"
  else:
    resultado += " mas não pode tirar habilitação"
  
  print(resultado)

else:
  print("Você não pode votar, muito menos tirar a habilitação")