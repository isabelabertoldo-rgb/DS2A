import random

cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
numero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

cor_mesa = random.choice(cores)
numero_mesa = random.choice(numero)
print(f"Carta na mesa: {numero_mesa} {cor_mesa}")
    
cor_jogador = random.choice(cores)
numero_jogador = random.choice(numero)

print(f"Você tem uma carta: {numero_jogador} {cor_jogador}")

if cor_jogador == cor_mesa or numero_jogador == numero_mesa:
    print("Você pode descartar essa carta!")
else:
    print("Você nao tem uma carta dessa, compre outra carta!")