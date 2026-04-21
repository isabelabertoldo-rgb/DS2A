idades = [12, 25, 17, 30, 14, 19]
maiores = []

for idade in idades:
    if idade >=18:
        maiores.append(idade)

print(f"Das idades {idades}, apenas {maiores} são maiores de 18.")