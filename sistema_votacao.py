idade = int(input("Idade: "))
if idade == 16 or idade == 17 or idade > 70:
    print(f"Com {idade} anos, o seu voto é opcional.")
else:
    print(f"Com {idade} anos, verifique se o seu voto é obrigatório.")