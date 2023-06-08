m = int(input("Insira um valor para m: "))
n = int(input("Insira um valor para n: "))
resultado = m

while m < n:
    m = int(input("Insira um valor para m maior do que n: "))

while m > n:
    resultado += m - 1
    m -= 1

print(f'O resultado da soma é {resultado}')