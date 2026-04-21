total_notas = 0
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    total_notas = total_notas + nota

media = total_notas / 4
print(f"A média das 4 notas é: {media:.1f}")