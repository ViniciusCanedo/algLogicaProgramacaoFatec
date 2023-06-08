import random

# Criar um dicionário para armazenar a contagem de cada soma
frequencia_somas = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Simular 30.000 jogadas dos dados
for _ in range(30000):
    dado1 = random.randint(1, 6)  # Jogada do primeiro dado
    dado2 = random.randint(1, 6)  # Jogada do segundo dado
    soma = dado1 + dado2  # Calcular a soma das faces

    frequencia_somas[soma] += 1  # Incrementar a contagem da soma

# Mostrar a frequência de cada soma
print("Frequência de cada soma:")
for soma, frequencia in frequencia_somas.items():
    print("Soma", soma, ":", frequencia)

# Calcular a frequência relativa do valor 7
frequencia_7 = frequencia_somas[7]
frequencia_total = sum(frequencia_somas.values())
frequencia_relativa_7 = frequencia_7 / frequencia_total

# Verificar se o valor 7 corresponde a 1/6 das jogadas
print("Frequência relativa do valor 7:", frequencia_relativa_7)
print("Aproximadamente 1/6:", abs(frequencia_relativa_7 - 1/6) < 0.01)
