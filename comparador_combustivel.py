p_alc = float(input("Preço do Alcool:"))
p_gas = float(input("Preço da Gasolina:"))
if p_alc < (p_gas * 0.7):
    print(f"Com o alcool a R$ {p_alc:.2f}, vale a pena abastecer com alcool")
else: 
    print(f"Com a gasolina a R$ {p_gas:.2f}, vale a pena abastecer com gasolina")