print("Números entre 1 e 50 que são divisíveis por 5 E por 2:")
for i in range(1, 51):
    # Verifica se o número atende aos dois critérios
    if i % 5 == 0 and i % 2 == 0:
        print(f"Achei: {i}")