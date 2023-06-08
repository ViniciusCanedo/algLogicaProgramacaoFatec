minutos = 10
segundos = 0

print(f"{minutos}:{segundos}")

for i in range(600):
    if(minutos != 0 and segundos == 0):
        minutos -= 1
        segundos = 59

        print(f"{minutos}:{segundos}")
    elif (segundos != 0 ):
        segundos -= 1
        print(f"{minutos}:{segundos}")
    elif (minutos == 0 and segundos == 0):
        print(f"{minutos}:{segundos}")
        break
    