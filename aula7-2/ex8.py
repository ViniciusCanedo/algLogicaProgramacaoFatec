n = int(input("Verifique se um número é primo: "))
count = 0
i = 1
while i <= n:
    if (n % i == 0):
        count += 1
    i += 1

if(count == 2):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")