mar = [
    [0,1,0],
    [0,0,0],
    [1,0,0]
]

tentativas = 2
while tentativas > 0:
    print(f"\n Você tem {tentativas} bombas!")
    l = int(input("Escolha a linha (0-2):"))
    c = int(input("Escolha a coluna (0-2):"))
    
    if mar [l][c]==1:
        print("BUM! Você acertou o navio!")
        mar[l][c] = 0
        tentativas = 0
    else:
        tentativas = tentativas -1
        print("Água... Tente novamente.")
        
print("Fim do Jogo!")