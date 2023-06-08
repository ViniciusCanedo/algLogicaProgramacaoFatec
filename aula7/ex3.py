somaAltura = 0
somaPeso = 0
minImc = 1000
maxImc = 0
for i in range(1, 21):
    altura = float(input(f"Insira a {i}ª altura: "))
    peso = float(input(f"Insira a {i}º peso: "))

    somaAltura += altura
    somaPeso += peso

    imc = peso / (altura ** 2)

    if(imc >= maxImc):
        maxImc = imc
    elif(imc <= minImc):
        minImc = imc

print(f"A média das alturas é {somaAltura / 20}")
print(f"A média dos pesos é {somaPeso / 20}")
print(f"O menor IMC é {minImc}")
print(f"O maior IMC é {maxImc}")