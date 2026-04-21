produtos = []

for i in range (3):
    nome = input(f"Nome do Produto {i+1}:")
    preco = float(input(f"Preço de {nome}"))
    produtos.append([nome, preco])
    
    print ("\n--- RELATÓRIO DE PREÇOS ---")
    for p in produtos:
        if p[1] > 100 or p[0] =="Especial":
            print(f"PRODUTO VIP: {p[0]} custa R$ {p[1]:.2f}")
        else:
            print(f"Produto Comum: {p[0]} custa R$ {p[1]:.2f}")