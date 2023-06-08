hora = float(input("Insira o horário (horas.minutos): "))
horaInt = int(hora)
minutos = (hora - horaInt) * 100
horaMin = (horaInt * 60) + minutos

print(f'{hora} horas = {horaMin} minutos')