media = float(input("Média: "))
presenca = int(input("Presença (%): "))
if media >= 6.0 and presenca >= 75:
    print(f"Aprovado com média {media} e {presenca}% de presença.")
else:
    print(f"Reprovado. Status: Média {media}, Presença {presenca}%.")