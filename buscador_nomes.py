nomes = ["Helena", "Julio", "Nataly", "Matheus"]
busca = input("Quem você deseja buscar?"). capitalize()

if busca in nomes:
    print(f"Sim, {busca} está na lista")
else:
    print(f"O nome {busca} não foi encontrado.")