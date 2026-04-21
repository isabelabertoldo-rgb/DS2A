renda = float(input("Renda: "))
meses = int(input("Meses de trabalho: "))
if renda >= 2500 and meses >= 12:
    print(f"Empréstimo aprovado para renda de R$ {renda:.2f}.")
else:
    print(f"Empréstimo negado. Requisitos mínimos não atingidos.")