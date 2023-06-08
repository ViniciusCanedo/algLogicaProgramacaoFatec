import random

frequencia_faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(6000):
    resultado = random.randint(1, 6) 
    frequencia_faces[resultado] += 1  


print("Frequência de sorteio de cada face:")
for face, frequencia in frequencia_faces.items():
    print("Face", face, ":", frequencia)
