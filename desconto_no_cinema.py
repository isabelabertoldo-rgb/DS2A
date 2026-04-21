idade = int(input("Sua idade: "))
carteirinha = input("Tem carteirinha? (s/n): ")
if idade < 12 or carteirinha == "s":
    print(f"Critério atendido. Você tem direito a meia-entrada!")
else:
    print(f"Idade {idade} e sem carteirinha: paga inteira.")