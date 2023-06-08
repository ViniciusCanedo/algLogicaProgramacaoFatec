inicio = 0
posterior = 1

print(inicio)
print(posterior)

for i in range (8):
    final = inicio + posterior
    print(final)
    substituto = posterior
    posterior = final
    inicio = substituto