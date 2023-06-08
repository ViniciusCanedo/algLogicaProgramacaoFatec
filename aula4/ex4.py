import datetime

dataNasc = input("Insira sua data de nascimento (dd/mm/aaaa):")
separarData = dataNasc.split("/")
anoNasc = int(separarData[2])
mesNasc = int(separarData[1])
diaNasc = int(separarData[0])

d1 = datetime.datetime(anoNasc, mesNasc, diaNasc)
d2 = datetime.datetime.now()

diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30
weeks, days = days // 7, days % 7

print("Você tem {} anos, {} meses, {} semanas e {} dias".format(years, months, weeks, days))