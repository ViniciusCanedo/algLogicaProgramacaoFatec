inicio = 0
posterior = 1
i = 1

print(inicio)
print(posterior)

while i <= 8:
    final = inicio + posterior
    print(final)
    substituto = posterior
    posterior = final
    inicio = substituto

    i += 1