valor = float(input("Valor da compra: "))
cupom = input("Tem cupom? (s/n): ")
if valor > 200 or cupom == "s":
    print(f"Parabéns! Na compra de R$ {valor:.2f}, o frete é grátis.")
else:
    print(f"Compra de R$ {valor:.2f} sem cupom: frete fixo de R$ 20,00.")