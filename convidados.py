convidados = []
for indice in range (1,4):
    nome = input("Digite o nome do convidado {indice}")
    convidados.append(nome)

print(f"Sua lista de convidados tem {len(convidados)} pessoas: {convidados}")