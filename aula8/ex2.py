data = input("Insira uma data (dd/mm/aaaa): ")

data = data.split("/")

print(f"{data[2]}{data[1]}{data[0]}")