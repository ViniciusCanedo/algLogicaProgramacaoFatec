def converter_para_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos


horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

total_segundos = converter_para_segundos(horas, minutos, segundos)
print("O total de segundos é:", total_segundos)
