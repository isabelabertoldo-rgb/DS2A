idade = int(input("Idade: "))
if idade >= 5 and idade <= 10:
    categoria = "Infantil"
elif idade >= 11 and idade <= 17:
    categoria = "Juvenil"
elif idade >= 18:
    categoria = "Adulto"
else:
    categoria = "Não permitida"
print(f"Atleta com {idade} anos está na categoria: {categoria}.")