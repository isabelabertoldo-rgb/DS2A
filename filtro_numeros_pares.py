limite = int(input("Até qual número quer ver os pares? "))
for n in range(1, limite + 1):
    if n % 2 == 0:
        print(f"O número {n} é par.")