segredo = 7
tentativas = 3

print("Adivinhe o número secreto (1 a 10). Você tem 3 chances!")

while tentativas > 0:
    chute = int(input(f"Tentativas restantes ({tentativas}): "))
    
    if chute == segredo:
        print(f"Parabéns! O número era {segredo}.")
        tentativas = 0 # Quebra o loop
    else:
        tentativas = tentativas - 1
        if tentativas > 0:
            print("Errou! Tente de novo.")
        else:
            print(f"Suas chances acabaram. O número era {segredo}.")