notas = []
for i in range (1,5):
    n = float(input(f"Digite a nota{i:}:"))
    notas.append(n)

media = sum(notas)/len(notas)
print(f"Notas registradas: {notas}")
print(f"A média da turma é: {media:.1f} ")