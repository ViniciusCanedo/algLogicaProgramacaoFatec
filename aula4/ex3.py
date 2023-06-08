anoNasc = int(input("Insira o ano de seu nascimento: "))
anoAtual = int(input("Insira o ano atual: "))
idadeAno = anoAtual - anoNasc
idadeMes = idadeAno * 12
idadeDia = idadeAno * 365
idadeSemana = idadeAno * 52

print(f'sua idade é {idadeAno} anos, {idadeMes} meses, {idadeDia} dias, {idadeSemana}')