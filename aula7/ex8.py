n = int(input("Verifique se um número é primo: "))
count = 0

for i in range(1, n + 1):
    if (n % i == 0):
        count += 1

if(count == 2):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")